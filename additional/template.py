#!/usr/bin/env python

import os
from pathlib import Path

total_count = 0

def process_project(project_path):
    global total_count
    for path in Path(project_path).rglob('*serverless*.y*ml'):
        total_count += 1
        #print(path)

if __name__ == '__main__':
    users = [f.path for f in os.scandir('serverless-dataset') if f.is_dir()]
    projects = []
    for user in users:
        projects += [f.path for f in os.scandir(user) if f.is_dir()]

    print('{} Projects found.'.format(len(projects)))

    for project in projects:
        process_project(project)

    print('{} candidate ymls found.'.format(total_count))
