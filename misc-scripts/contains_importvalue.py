import os
import traceback
import yaml
from pathlib import Path
import pandas as pd

total_count = 0
provider_count = {}

def parse_provider(config):
    if 'provider' not in config:
        return None

    provider = config['provider']

    if not isinstance(provider, dict):
        return None

    if 'name' in provider:
        return provider['name']

    return None



def process_project(project_path):
    global total_count
    global provider_count

    for path in Path(project_path).rglob('*serverless*.y*ml'):
        total_count += 1

        with open(path, 'r') as file:
            try:
                config = yaml.safe_load(file)
                if not isinstance(config, dict):
                    continue

                provider = parse_provider(config)
                if not provider in provider_count:
                    provider_count[provider] = 0
                provider_count[provider] += 1
            except yaml.constructor.ConstructorError:
                continue
            except yaml.scanner.ScannerError:
                continue
            except yaml.composer.ComposerError:
                continue
            except yaml.parser.ParserError:
                continue
            except Exception as e:
                print(traceback.format_exc())
                continue


if __name__ == '__main__':
    count = 0
    with open('data/sec-policy-only.csv', 'r') as files:
        header = True
        for line in files.readlines():
            if header:
                header = False
                continue
            with open(line.strip(), 'r') as yml:
                hasImport = False
                for yml_line in yml.readlines():
                    if '::ImportValue' in yml_line:
                        hasImport = True
                        break
                if hasImport:
                    count += 1

    print(count)