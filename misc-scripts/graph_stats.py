import multiprocessing
from pyparsing import line_end
from pyswip import Prolog
import os
from datetime import date, datetime

from multiprocessing import Process

expected_resources = [
    'kms', 'kinesis', 'secretsmanager', 'ses',
    'execute-api', 's3', 'ssm', 'es',
    'iam', 'cognito-idp', 'dynamodb', 'sqs',
    'states', 'logs', 'sns', 'rds', 'sdb'
]

def format_timedelta_to_HHMMSS(td):
    td_in_seconds = td.total_seconds()
    hours, remainder = divmod(td_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    hours = int(hours)
    minutes = int(minutes)
    seconds = seconds
    if minutes < 10:
        minutes = "0{}".format(minutes)
    if seconds < 10:
        seconds = "0{}".format(seconds)
    return "{}:{}:{}".format(hours, minutes, seconds)

def basic_stats(f, q):
    prolog = Prolog()
    prolog.consult(f)
    output = {}
    output['total_fns'] = 0
    output['public_fns'] = 0
    output['private_fns'] = 0
    output['total_res'] = 0
    output['public_r_res'] = 0
    output['public_w_res'] = 0
    output['public_rw_res'] = 0
    output['private_res'] = 0
    output['full_wcp_full_wcr'] = 0 # full wc perm on full wc res
    output['any_wcp_any_wcr'] = 0 # anywildcard perm on anywildcard res
    output['full_wcp_any_r'] = 0 # full wildcard on any resource
    output['any_p_full_wcr'] = 0 # any perm on full wildcard resource
    output['half_wcp_any_r'] = 0 # full wildcard on any resource
    output['any_p_half_wcr'] = 0 # any perm on full wildcard resource
    output['half_wcp_half_wcr'] = 0 # half wildcard perm on full wildcard resource
    output['event sns'] = 0
    output['event stream'] = 0
    output['event s3'] = 0
    output['event iot'] = 0
    output['total_resources'] = 0
    output['resources'] = {}
    for key in expected_resources:
        output['resources'][key] = 0

    try:
        for result in prolog.query("function(A, B), A\==''."):
            output['total_fns'] +=1
            if result['B'].lower() == 'true':
                output['public_fns'] += 1
            else:
                output['private_fns'] += 1

        for result in prolog.query("resource(A, B, C, D), A\==''."):
            output['total_res'] += 1
            if result['C'].lower() == 'true' and result['D'].lower() == 'true':
                output['public_rw_res'] += 1
            elif result['C'].lower() == 'true':
                output['public_r_res'] += 1
            elif result['D'].lower() == 'true':
                output['public_w_res'] += 1
            else:
                output['private_res'] += 1

        # WC combinations
        # any = no wildcard or contains wildcard
        # nowildcard = explicit permission e.g., 's3:PutObject'
        # halfwildcard = 's3:*' or 'res*'
        # fullwildcard = '*'
        # anywildcard =  fullwildcard or halfwildcard but not nowildcard

        for result in prolog.query("wildcards(Func, Perm, Res, [perm(fullwildcard), res(fullwildcard)])."):
            output['full_wcp_full_wcr'] += 1

        for result in prolog.query("wildcards(Func, Perm, Res, [perm(anywildcard), res(anywildcard)])."):
            output['any_wcp_any_wcr'] += 1

        for result in prolog.query("wildcards(Func, Perm, Res, [perm(fullwildcard), res(any)])."):
            output['full_wcp_any_r'] += 1

        for result in prolog.query("wildcards(Func, Perm, Res, [perm(any), res(fullwildcard)])."):
            output['any_p_full_wcr'] += 1

        for result in prolog.query("wildcards(Func, Perm, Res, [perm(halfwildcard), res(any)])."):
            output['half_wcp_any_r'] += 1

        for result in prolog.query("wildcards(Func, Perm, Res, [perm(any), res(halfwildcard)])."):
            output['any_p_half_wcr'] += 1

        for result in prolog.query("wildcards(Func, Perm, Res, [perm(halfwildcard), res(halfwildcard)])."):
            output['half_wcp_half_wcr'] += 1
        
        for result in prolog.query("event_sns_msg(A, B), A\=='', B\==''."):
            output['event sns'] += 1

        for result in prolog.query("event_stream_msg(A, B), A\=='', B\==''."):
            output['event stream'] += 1

        for result in prolog.query("event_s3(A, B, C), A\=='', B\=='', C\==''."):
            output['event s3'] +=1

        for result in prolog.query("event_iot(A), A\==''."):
            output['event iot'] += 1

        for result in prolog.query("resource(A, B, C, D), A\=='', B\==''."):
            res_type = result['A']
            if res_type not in output['resources']:
                output['resources'][res_type] = 0
            output['resources'][res_type] += 1

        total_resources = 0
        for _, count in output['resources'].items():
            total_resources += count
        output['total_resources'] = total_resources
            
    except Exception as e:
        print('Error processing {}'.format(f))
        print(e)
        input('>')

    q.put(output)


def path_stats(f, q):
    prolog = Prolog()
    prolog.consult(f)
    output = {}
    output['read_paths'] = 0
    output['explicit_r_paths'] = 0
    output['write_paths'] = 0
    output['explicit_w_paths'] = 0
    output['rw_paths'] = 0
    output['explicit_rw_paths'] = 0
    output['exfil'] = 0
    output['explicit_exfil_paths'] = 0

    try: 
        for result in prolog.query("find_read_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs)."):
            print(result)
            output['read_paths'] += 1

        for result in prolog.query("find_write_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs)."):
            print(result)
            output['write_paths'] += 1

        for result in prolog.query("find_rw_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs)."):
            print(result)
            output['rw_paths'] +=1

        for result in prolog.query("exfil_to_public_res(EntryPoint, PrivRes, PubRes, RPath, REdges, RLength, RCFs, RDFs, REFs, WPath, WEdges, WLength, WCFs, WDFs, WEFs)."):
            print(result)
            output['exfil'] +=1
    except Exception as e:
        print('Error processing {}'.format(f))
        print(e)
        input('>')

    q.put(output)

# input pl file path 
def path_stats(f):
    prolog = Prolog()
    prolog.consult(f)
    output = {}
    output['read_paths']=[]
    output['write_paths']=[]
    output['rw_paths']=[]
    

    try: 
        for result in prolog.query("find_read_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs)."):
            output['read_paths'].append(result)

        for result in prolog.query("find_write_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs)."):
            output['write_paths'].append(result)

        for result in prolog.query("find_rw_paths(Func, TargetRes, false, false, Path, Edges, [], Funcs, Length, CFs, DFs, EFs)."):
            output['rw_paths'].append(result)

        #for result in prolog.query("exfil_to_public_res(EntryPoint, PrivRes, PubRes, RPath, REdges, RLength, RCFs, RDFs, REFs, WPath, WEdges, WLength, WCFs, WDFs, WEFs)."):
            #print(result)
    except Exception as e:
        print('Error processing {}'.format(f))
        print(e)
        input('>')

    return output



if __name__ == '__main__':
    result_count = 0
    read_count = 0
    write_count = 0
    rw_count = 0
    exfil_count = 0
    query_timeout = 60*60*12
    slow_files = set()
    process_count = 0

    full_runtime_start = datetime.now()

    with open('data/prolog-results.csv', 'w') as outfile:
        outfile.write(
            'file,total_fns,public_fns,private_fns,' +\
            'total_res,public_r_res,public_w_res,public_rw_res,private_res,' +\
            'full_wcp_full_wcr,any_wcp_any_wcr,' +\
            'full_wcp_any_r,any_p_full_wcr,half_wcp_any_r,any_p_half_wcr,half_wcp_half_wcr,' +\
            'event_sns,event_stream,event_s3,event_iot,' +\
            'total_resources,'
        )

        for res in expected_resources:
            outfile.write(f'{res},')

        outfile.write(
            'r_path,explicit_r_paths,w_paths,explicit_w_paths,' +\
            'rw_paths,explicit_rw_paths,exfil_paths,explicit_exfil_paths,runtime\n'
        )
        for filename in os.listdir('data/new-results'):
            f = os.path.join('data/new-results', filename)

            # skip files taking very long for later analysis
            if f in []:
                print('Skipping {}'.format(f))
                continue

            start_time = datetime.now()
            process_count += 1
            print(f'{process_count}. Analyzing {f} ', end='')
            q = multiprocessing.Queue()
            p = Process(target=basic_stats, args=(f,q))
            p.start()

            try:
                res = q.get() # no timeout this should always finish
                outfile.write(
                    f"{f},{res['total_fns']},{res['public_fns']},{res['private_fns']}," +\
                    f"{res['total_res']},{res['public_r_res']},{res['public_w_res']}," +\
                    f"{res['public_rw_res']},{res['private_res']}," +\
                    f"{res['full_wcp_full_wcr']},{res['any_wcp_any_wcr']}," +\
                    f"{res['full_wcp_any_r']},{res['any_p_full_wcr']},{res['half_wcp_any_r']},{res['any_p_half_wcr']},{res['half_wcp_half_wcr']}," +\
                    f"{res['event sns']},{res['event stream']},{res['event s3']},{res['event iot']},"
                )

                outfile.write( f"{res['total_resources']},")
                for res_type in expected_resources:
                    outfile.write(f"{res['resources'][res_type]},")
            except Exception as e:
                print(e)
                input('Error processing basic stats>')


            p = Process(target=path_stats, args=(f,q))
            p.start()
            
            try:
                res = q.get(timeout=query_timeout)
                has_path = False
                if res['read_paths'] > 0:
                    read_count += 1
                    has_path = True
                    
                if res['write_paths'] > 0:
                    write_count += 1
                    has_path = True

                if res['rw_paths'] > 0:
                    rw_count += 1
                    has_path = True

                if res['exfil'] > 0:
                    exfil_count += 1
                    has_path = True

                if has_path:
                    result_count +=1 

                end_time = datetime.now()
                runtime = format_timedelta_to_HHMMSS(end_time - start_time)
                print(f'- {runtime}')

                outfile.write(
                    f"{res['read_paths']},{res['explicit_r_paths']}," +\
                    f"{res['write_paths']},{res['explicit_w_paths']}," +\
                    f"{res['rw_paths']},{res['explicit_rw_paths']}," +\
                    f"{res['exfil']},{res['explicit_exfil_paths']},{runtime}\n"
                )

                if res['exfil'] > 0:
                    print(f'{f} has an exfil path')
                p.join()
            except Exception as e:
                outfile.write('0,0,0,0,0,0,0,0,ERROR\n')
                #print(e)
                #print('Processing took over {} seconds'.format(query_timeout))
                print('timed out')
                slow_files.add(f)
                p.kill()

    print('{} files had some kind of path.'.format(result_count))
    print(f'{read_count} files had read path.')
    print(f'{write_count} files had write path.')
    print(f'{rw_count} files had read/write path.')
    print(f'{exfil_count} files had exfil path.')

    print(f'Full runtime {format_timedelta_to_HHMMSS(datetime.now() - full_runtime_start)}')
    print('Files that timed out: {}'.format(slow_files))

