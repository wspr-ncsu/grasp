#!/usr/bin/env python3

import re
import hashlib

var_cache = {}
resolve_map = {}

def jsonNotationToDictActions(input):
    matches = re.findall('(\w+)|\[(\d+)\]', input)
    actions = []
    for match in matches:
        if match[0]:
            actions.append(match[0])
        elif match[1]:
            actions.append(int(match[1]))

    return actions

def ResolveOther(string):
    global resolve_map
    var_type = string.split(':')[0]

    if var_type not in resolve_map:
        resolve_map[var_type] = 0

    retval = var_type + str(resolve_map[var_type])

    resolve_map[var_type] += 1

    return retval


def ResolveSelf(string):
    pass

def ResolveVariable(string):
    global var_cache

    match = re.search('\${([^,]*)(,.*)?}', string)
    if match:
        try:
            first_var = match.group(1)

            if first_var in var_cache:
                return var_cache[first_var]

            if 'self:' in first_var:
                ResolveSelf(first_var)
            else:
                resolved_value = ResolveOther(first_var)
        except:
            pass
        if match.group(3):
            return match.group(3).split(',')[1].strip().replace("'", '').replace('"', '')
        else:
            return hashlib.sha256(match.group(0).encode('utf-8')).hexdigest()[:16]
    else:
        return string

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
        elif input[index] == '}':
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


print(ResolveString('${file(${env:test-${opt:test}}-${opt:extra})}'))
print(ResolveString("${opt:help, 'no'}"))
print(ResolveString('${opt:help, "nope"}'))
print(ResolveString("${opt:help, none}"))
print(ResolveString(""))





# mydict = {'one': [{'two': ['a', 'b']}]}
# val = mydict
# for action in jsonNotationToDictActions('one[0].two[1]'):
#     val = val[action]
# print(val)
