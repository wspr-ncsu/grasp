import re
import hashlib

variable_cache = {} # (value, is real value)
fake_variable_map = {}
config = {}

def jsonNotationToDictActions(input):
    matches = re.findall('(\w+)|\[(\d+)\]', input)
    actions = []
    for match in matches:
        if match[0]:
            actions.append(match[0])
        elif match[1]:
            actions.append(int(match[1]))

    return actions

def isVariable(string):
    if re.search('(self|opt|sls|env|cf|s3|ssm|aws):.*', string):
        return True
    else:
        return False

def generateFakeValue(string, full_expr=False):
    global fake_variable_map
    if full_expr:
        return 'FAKE-EXP-{}'.format(hashlib.sha256(string.encode('utf-8')).hexdigest()[:16])
    else:
        if match := re.search('(.*):.*', string):
            var_type = match.group(1).lower()
            if var_type not in fake_variable_map:
                fake_variable_map[var_type] = 0

            retval = 'FAKE-{}-{}'.format(var_type.upper(), fake_variable_map[var_type])
            fake_variable_map[var_type] += 1

            return retval
        else:
            raise ValueError('Could not generate fake value for {}'.format(string))
            
def VariableValue(string):
    global config
    if match := re.search('self:(.*)', string):
        try:
            val = config
            jsonNotation = match.group(1)
            for action in jsonNotationToDictActions(jsonNotation):
                val = val[action]

            if isinstance(val, dict):
                for key in val.keys():
                    if 'Fn::' in key or key == 'Ref':
                        raise NotImplementedError('Functions and refs not handled')

            return (val, True)
        except KeyError as e:
            if jsonNotation.lower() == 'provider.region':
                return ('us-east-1', True)
            elif jsonNotation.lower() == 'provider.stage':
                return ('dev', True)
            
            return (generateFakeValue(string), False)
    else:
        return (generateFakeValue(string), False)

def ResolveVariable(string):
    global variable_cache

    if string in variable_cache:
        return variable_cache[string][0]

    match = re.search('\${([^,]*)(,.*)?}', string)

    if match is None:
        return string

    first_var = match.group(1)

    if first_var not in variable_cache:
        variable_cache[first_var] = VariableValue(first_var)

    if match.group(2) is None:
        return variable_cache[first_var][0]
    else:
        # Must parse a default value
        default = match.group(2).replace(',', '').strip()
        default_is_real = False

        if isVariable(default):
            if default not in variable_cache:
                variable_cache[default] = VariableValue(default)
            
            default_value, default_is_real = variable_cache[default]
        else:
            default_is_real = True
            if default[0] in ['"', "'"]:
                if default[0] == default[-1]:
                    default_value = default.replace(default[0], '')
                else:
                    default_value = default

        first_value, first_is_real = variable_cache[first_var]

        if first_is_real:
            variable_cache[string] = (first_value, first_is_real)
            return first_value
        elif default_is_real:
            variable_cache[string] = (default_value, default_is_real)
            return default_value
        else:
            fake_value = generateFakeValue(string, True)
            variable_cache[string] = (fake_value, False)
            return fake_value

def ResolveString(input):
    if len(input) == 0:
        return ''

    index = 0
    variable_starts = []
    while True:
        if index >= len(input):
            return input

        # variables begin with ${. add the beginning location of each variable 
        if input[index] == '$' and (index + 1 < len(input)) and input[index + 1] == '{':
            variable_starts.append(index)
        
        # variables end with }. when encountered we have a non-nested variable to replace with a string
        elif input[index] == '}' and len(variable_starts) > 0:
            # Get the string before and after the current variable
            before = input[:variable_starts[-1]]
            after = input[index + 1:]

            # Get the current variable (including ${...})
            var = input[variable_starts[-1]:index + 1]

            # Convert the variable into a string (or a hash if we can't resolve it)
            resolved_var = ResolveVariable(var)

            # Place the resolved variable after the old beginning of input
            input = before + resolved_var

            # Update index to point at last character of string just replaced
            index = len(input) - 1

            # Add the remaining text not yet parsed
            input = input + after

            # Remove the beginning index of variable just resolved
            variable_starts.pop()
        index += 1

# print(ResolveVariable('${file(${env:test-${opt:test}}-${opt:extra})}'))
# print(ResolveVariable("${opt:help, 'no'}"))
# print(ResolveVariable('${opt:help}'))
# print(ResolveVariable("${opt:help, opt:hello}"))

#with open('/data/serverless-dataset/mozilla/service-map/serverless.yml', 'r') as infile:
with open('/data/serverless-ac21/analysis/misc-scripts/working-ymls.csv', 'r') as infile:
    vars = set()
    process = False
    for line in infile:
        if not process:
            process = True
            continue

        with open(line.strip(), 'r') as yml:
            for yml_line in yml:
                if yml_line.strip().startswith('#'):
                    continue

                try:
                    if '${file(' not in yml_line:
                        print(ResolveString(yml_line).strip('\n'))
                    else:
                        print(yml_line.strip('\n'))
                except Exception as e:
                    print(e)
                    print(line)
                    input('>')