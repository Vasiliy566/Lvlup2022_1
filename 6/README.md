# Задачка 1.
Написать программу, которая считывает из консоли пусть до файла и файл и выводит самое длинное слово, если такое файл есть, и выводит "Not Found" если такого слова нет


### Примеры ввода

#### Пример 1
```
example.txt:
a
bb
ccc
dddd
```

Input:
    
    /data/example.txt
    
Output:
    
    dddd

#### Пример 2
  
Input:
    
     /data/example2.txt
    
Output:
    
    "Not found"

### Примечание
Проверить налечие файла можно двумя способами:

1. 
```
from os.path import exists
file_exists = exists(path_to_file)
# file_exists - True/False, в зависимости от наличия файла
```

2.
```
from pathlib import Path

path_to_file = 'readme.txt'
path = Path(path_to_file)

if path.is_file():
    print(f'The file {path_to_file} exists')
else:
    print(f'The file {path_to_file} does not exist')
```

# Задачка 2.
Создать файл с вопросами с вариантами ответа для викторины, создать файл с ответами. Реализовать викторину, которая будет спрашивать вопросы из файла с вопросами и сравнивать с файлом с ответами.

### Примечание
Рекомендуется хранить ответы и вопросы в формате ```json```
