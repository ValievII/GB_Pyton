from os import mkdir
from os.path import exists, join as path_join

base = 'my_project'

if not exists(base):
    mkdir(base)

for file in ['settings', 'mainapp', 'adminapp', 'authapp']:
    path = path_join(base, file)
    if not exists(path):
        open(path, 'a').close()