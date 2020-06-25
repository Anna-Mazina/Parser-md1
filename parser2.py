# Скрипт для обработки файлов формата *.md
# Обрабатывает все файлы, которые находятся с ним в одной папке


# -*- coding: utf-8 -*-

import os
import glob
import shutil

for infile in glob.glob("*.md"):
    with open(infile, "r") as file:  # открываем файлы из текущей из папки, в которой находится скрипт
        file.read().encode("utf-8", "ignore")  # Читаем и кодируем его в  utf-8
        lines = file.readlines()

    with open(infile, 'w') as f:  # Открываем файл и проводим обработку. Перезаписываем строки, в которых нет символов
        for line in lines:
            if ":::" not in line:
                if "<div>" not in line:
                    if "</div>" not in line:
                        f.write(line)

# Создаем новую папку и переносим обработанные файлы

os.mkdir("new_dir")
for a in glob.glob('*.md'):
    new_name = '{}_{}'.format(os.path.basename(os.path.dirname(a)), os.path.basename(a))
    shutil.move(a, os.path.join('new_dir', new_name))
print('Готово')
