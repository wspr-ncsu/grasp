from pathlib import Path
import yaml
import json
import os
import re
import hashlib
import traceback

class ServerlessProject(object):
    def __init__(self, path):
        self.root_dir = os.path.dirname(path)
        self.path = path
        self.variable_cache = {} # stores variable name --> (value, bool: real or fake) real means the value was in the config
        self.fake_variable_map = {} # Used to track unique names for fake variables
        self.manual_debug = False # stops on errors to wait for manual interaction and can recover

        yml_path = Path(self.path)
        if not yml_path.is_file:
            raise TypeError('yml is not a file {}'.format(self.path))

        with open(self.path, 'r') as yml_file:
            try:
                config = yaml.safe_load(yml_file)

                if not isinstance(config, dict):
                    raise TypeError('Parsed config is not a dictionary {}'.format(self.path))
            
                self.config = config
                self.ResolveDict(self.config)

                # Functions might be a list if each function is in a separate yaml
                if isinstance(self.config['functions'], list):
                    fn_dict = {}
                    for fn in self.config['functions']:
                        for fn_name, fn_value in fn.items():
                            fn_dict[fn_name] = fn_value
                    
                    self.config['functions'] = fn_dict

                # Similarly for resources
                if 'resources' in self.config:
                    if isinstance(self.config['resources'], list):
                        res_dict = {}
                        for list_res in self.config['resources']:
                            for res_name, res_value in list_res.items():
                                res_dict[res_name] = res_value
                        
                        self.config['resources'] = res_dict

                if 'provider' in self.config and 'name' in self.config['provider']:
                    if self.config['provider']['name'].lower() != 'aws':
                        raise TypeError('yml is not for aws {}'.format(self.path))
                if 'Fn::' in json.dumps(self.config):
                    raise NotImplementedError('YAML functions not handled')
                if self.hasUnresolvedFiles():
                    raise NotImplementedError('Ehh still unresolved files.')
            except yaml.constructor.ConstructorError:
                raise TypeError('Invalid yml: {}'.format(self.path))
            except yaml.scanner.ScannerError:
                raise TypeError('Invalid yml: {}'.format(self.path))
            except yaml.composer.ComposerError:
                raise TypeError('Invalid yml: {}'.format(self.path))
            except yaml.parser.ParserError:
                raise TypeError('Invalid yml: {}'.format(self.path))

    # Check for any reference of a file I may not have resolved in the config
    def hasUnresolvedFiles(self):
        if file := re.search('\${file\(.*\)', json.dumps(self.config)):
            return True
        
        return False

    # Traverse the value of each key to resolve files and variables.
    def ResolveDict(self, input):
        for key, value in input.items():
            # TODO if key is a Fn:: logic to resolve goes here
            if isinstance(value, dict):
                self.ResolveDict(value)
            elif isinstance(value, list):
                self.ResolveList(value)
            elif isinstance(value, str):
                if value.startswith('${file('):
                    obj = self.FilePathToObject(input[key])
                    input[key] = obj
                    if isinstance(obj, dict):
                        self.ResolveDict(obj)
                    elif isinstance(obj, list):
                        self.ResolveList(obj)
                    elif isinstance(obj, str):
                        # I'll be pissed if someone has a file resolve to a file
                        input[key] = self.ResolveString(obj)                    
                    elif isinstance(obj, int) or isinstance(obj, bool) or isinstance(obj, float):
                        pass
                    else:
                        raise NotImplementedError(
                            '{} not handled as returned object in ResolveDict: {}-{}'.format(type(obj), obj,self.config))
                else:
                    # If the string doesn't begin with ${file()} then resolve all other variables
                    # note file can be in the middle somewhere if it resolves a string property
                    input[key] = self.ResolveString(value)
                if '*' in value and value[-1] != '*':
                    input('mid value *>')
            elif isinstance(value, bool) or isinstance(value, int) or isinstance(value, float):
                pass
            elif value is None:
                input[key] = ''
            else:
                print(key)
                print(self.config)
                raise NotImplementedError('{} not handled in ResolveDict'.format(type(value)))
    
    # Traverse the value of each item in the list to resolve files and variables
    def ResolveList(self, input):
        for index in range(len(input)):
            value = input[index]
            if isinstance(value, list):
                self.ResolveList(value)
            elif isinstance(value, dict):
                self.ResolveDict(value)
            elif isinstance(value, str):
                if input[index].startswith('${file('):
                    obj = self.FilePathToObject(input[index])
                    input[index] = obj
                    if isinstance(obj, dict):
                        self.ResolveDict(obj)
                    elif isinstance(obj, list):
                        self.ResolveList(obj)
                    elif isinstance(obj, str):
                        input[index] = self.ResolveString(obj)
                    elif isinstance(obj, int) or isinstance(obj, bool) or isinstance(obj, float):
                        pass
                    else:
                        raise NotImplementedError('{} not handled as returned object in ResolveList: {}'.format(type(obj), obj))
                else:
                    # If the string doesn't begin with ${file()} then resolve all other variables
                    # note file can be in the middle somewhere if it resolves a string property
                    input[index] = self.ResolveString(value)
                if '*' in value and value[-1] != '*':
                    input('mid value *>')
            elif isinstance(value, bool) or isinstance(value, int) or isinstance(value, float):
                pass
            else:
                raise NotImplementedError('{} not handled in ResolveList'.format(type(value)))

    def ResolveVariable(self, string):
        if string in self.variable_cache:
            return self.variable_cache[string][0]

        if string.startswith('${file('):
            resovled_file = self.FilePathToObject(string)
            if not isinstance(resovled_file, str):
                raise TypeError('$\{file()\} in middle of string could not be resolved to string')
            return resovled_file

        match = re.search('\${([^,]*)(,.*)?}', string)

        if match is None:
            return string

        first_var = match.group(1)

        if first_var not in self.variable_cache:
            self.variable_cache[first_var] = self.VariableValue(first_var)

        if match.group(2) is None:
            return self.variable_cache[first_var][0]
        else:
            # Must parse a default value
            default = match.group(2).replace(',', '').strip()
            default_is_real = False

            if ServerlessProject.isVariable(default):
                if default not in self.variable_cache:
                    self.variable_cache[default] = self.VariableValue(default)
                
                default_value, default_is_real = self.variable_cache[default]
            else:
                default_is_real = True
                if default[0] in ['"', "'"]:
                    if default[0] == default[-1]:
                        default_value = default.replace(default[0], '')
                    else:
                        default_value = default

            first_value, first_is_real = self.variable_cache[first_var]

            if first_is_real:
                self.variable_cache[string] = (first_value, first_is_real)
                return first_value
            elif default_is_real:
                self.variable_cache[string] = (default_value, default_is_real)
                return default_value
            else:
                fake_value = self.generateFakeValue(string, True)
                self.variable_cache[string] = (fake_value, False)
                return fake_value
        
    # resolve any non-file variable, if no default is given and we don't have access to the variable
    # source (e.g., env) just resolve a hash for consistency. This will break files but no other way
    # to handle
    def ResolveString(self, input):
        if len(input) == 0:
            return ''

        index = 0
        variable_starts = []
        while True:
            if index >= len(input):
                # Check if we replaced a variable with another variable
                if re.search('\${.*}', input):
                    index = 0
                else:
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
                resolved_var = self.ResolveVariable(var)

                if isinstance(resolved_var, dict) or isinstance(resolved_var, list):
                    if index == len(input) - 1 and len(variable_starts) == 1:
                        return resolved_var
                    else:
                        raise ValueError('Error resolving variable')

                if isinstance(resolved_var, int):
                    resolved_var = str(resolved_var)
                # Place the resolved variable after the old beginning of input
                input = before + resolved_var

                # Update index to point at last character of string just replaced
                index = len(input) - 1

                # Add the remaining text not yet parsed
                input = input + after

                # Remove the beginning index of variable just resolved
                variable_starts.pop()
            index += 1

    def VariableValue(self, string):
        if match := re.search('self:(.*)', string):
            try:
                val = self.config
                jsonNotation = match.group(1)

                for action in ServerlessProject.jsonNotationToDictActions(jsonNotation):
                    val = val[action]

                if isinstance(val, dict):
                    for key in val.keys():
                        if isinstance(key, str) and ('Fn::' in key or key == 'Ref'):
                            raise NotImplementedError('Functions and refs not handled')

                return (val, True)
            except KeyError as e:
                if jsonNotation.lower() == 'provider.region':
                    return ('us-east-1', True)
                elif jsonNotation.lower() == 'provider.stage':
                    return ('dev', True)
                
                return (self.generateFakeValue(string), False)
            except TypeError as e:
                if isinstance(val, str):
                    return val
                
                raise e
        else:
            return (self.generateFakeValue(string), False)

    # Generates a fake value for a variable that could not be resolved in the config
    def generateFakeValue(self, string, full_expr=False):
        if full_expr:
            return 'FAKE-EXP-{}'.format(hashlib.sha256(string.encode('utf-8')).hexdigest()[:16])
        else:
            if match := re.search('(.*):.*', string):
                var_type = match.group(1).lower()
                if var_type not in self.fake_variable_map:
                    self.fake_variable_map[var_type] = 0

                retval = 'FAKE-{}-{}'.format(var_type.upper(), self.fake_variable_map[var_type])
                self.fake_variable_map[var_type] += 1

                return retval
            else:
                raise ValueError('Could not generate fake value for {}'.format(string))


    def FilePathToObject(self, file_string):
        if file_string is None:
            return {}

        extracted_file, property, default = ServerlessProject.ExtractFilePath(file_string)
        if extracted_file is None:
            return {}

        # YML files may have variables in path
        extracted_file = self.ResolveString(extracted_file)

        file_ext = extracted_file.split('.')[-1].lower()

        if file_ext != 'yml' and file_ext != 'yaml':
            raise NotImplementedError('No plans to resolve .{} files'.format(file_ext))

        file_path = os.path.join(self.root_dir, extracted_file)

        try:
            with open(file_path, 'r') as yml:
                config = yaml.safe_load(yml)

                if config is None:
                    raise ValueError('Resolved file contained empty config.')

                if property is not None:
                    resolved_property = self.ResolveString(property)
                    try:
                        for action in ServerlessProject.jsonNotationToDictActions(resolved_property):
                            config = config[action]

                        return config
                    except KeyError as e:
                        if default is not None:
                            return default

                        if self.manual_debug:
                            self.ManualDebug(file_string, self.path, self.config, e)
                            return ''

                        raise e
                    except Exception as e:
                        if self.manual_debug:
                            self.ManualDebug(file_string, self.path, self.config, e)
                            return ''
                        raise e

                else:
                    return config 
        except Exception as e:
            raise e

    def ManualDebug(self, *args):
        for arg in args:
            print(arg)

        input('>')

    @staticmethod
    def ExtractFilePath(file_variable):
        file_path = None
        property = None
        default = None
        if file := re.search('\${file\((.*)\)(:[^,]*)?(,.*)?}', file_variable):
            if file.group(1):
                file_path = file.group(1)

            if file.group(2):
                property = file.group(2)[1:]
            
            if file.group(3):
                default = file.group(3).replace(',', '')

        return file_path, property, default

    # Take javascript json dot notation and convert into strings and ints for dict/list access
    @staticmethod
    def jsonNotationToDictActions(input):
        matches = re.findall('(\w+)|\[(\d+)\]', input)
        actions = []
        for match in matches:
            if match[0]:
                actions.append(match[0])
            elif match[1]:
                actions.append(int(match[1]))

        return actions

    @staticmethod
    def isVariable(string): 
        if re.search('(self|opt|sls|env|cf|s3|ssm|aws):.*', string):
            return True
        else:
            return False

    # https://gist.github.com/gene1wood/5299969edc4ef21d8efcfea52158dd40 credit @afosterw
    @staticmethod
    def ParseArn(arn):
        # http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
        elements = arn.split(':', 5)
        result = {
            'arn': elements[0],
            'partition': elements[1],
            'service': elements[2],
            'region': elements[3],
            'account': elements[4],
            'resource': elements[5],
            'resource_type': None
        }
        if '/' in result['resource']:
            result['resource_type'], result['resource'] = result['resource'].split('/',1)
        elif ':' in result['resource']:
            result['resource_type'], result['resource'] = result['resource'].split(':',1)
        return result