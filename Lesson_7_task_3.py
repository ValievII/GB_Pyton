from os import mkdir, sep, walk
from os.path import exists, join as path_join
from shutil import copy2

paths = {} # словарь путей файлов
paths_dirs = [] # папки для создания
base_dir = 'my_project'

for root, dirs, files in walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            template = path_join(*root.split(sep)[-1:]) # наименование шаблона
            if template not in paths:
                # добавляем путь к шаблону в список для копирования
                paths_dirs.append(path_join(base_dir, 'templates', template))

            path_to_html = path_join(root, file)
            paths.update({path_to_html: path_join(base_dir, 'templates', template, file)})

# создаём основную папку, в которой будут шаблоны
if not exists(path_join(base_dir, 'templates')):
    mkdir(path_join(base_dir, 'templates'))

# создаём папки шаблонов
for d in paths_dirs:
    if not exists(d):
        mkdir(d)
        print(f'Папка {d} создана')

for old, new in paths.items():
    if not exists(new):
        copy2(old, new)
        print(f'Файл {old} скопирован в {new}')