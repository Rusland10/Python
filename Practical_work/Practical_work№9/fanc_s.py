import os
from docx2pdf import convert
from pdf2docx import parse
from PIL import Image


def start_directory():  # path
    return os.getcwd()


def list_file(*args):
    files = []
    files_c = []
    for filename in os.listdir(start_directory()):
        if filename.endswith(args):
            files.append(filename)
    for filename in enumerate(files, start=1):
        files_c.append(filename)
    return files_c


def menu():
    menu = [
            '1. Удалить все файлы начинающиеся на определенную подстроку',
            '2. Удалить все файлы заканчивающиеся на определенную подстроку',
            '3. Удалить все файлы содержащюю на определенную подстроку',
            '4. Удалить все файлы по расширению',
            '5. Удалить определенный файл'
            ]
    list_command = range(1, 6)
    print("Выберите действие:\n", *menu, sep='\n')
    input_user = int(input('Ваш выбор: '))
    while input_user not in list_command:
        input_user = int(input())
    return input_user


def directory():  # 0
    n = input('Введите путь: ')
    while n == '':
        n = input('Введите путь: ')
    os.chdir(n)
    return 'Успех'


def p2d():  # 1
    for i in list_file('pdf'):
        print(*i)
    n = int(input('Выберите файл: '))
    if n != 0:
        for i in list_file('pdf'):
            if i[0] == n:
                parse(i[1])
                return 'Успех'
    else:
        return


def d2p():  # 2
    for i in list_file('docx', 'doc'):
        print(*i)
    n = int(input('Выберите файл: '))
    if n != 0:
        for i in list_file('docx', 'doc'):
            if i[0] == n:
                convert(i[1])
                return 'Успех'
    else:
        return


def compression():  # 3
    for i in list_file('png', 'jpg', 'gif'):
        print(*i)
    n = int(input('Выберите файл: '))
    if n != 0:
        quality = int(input('Ведите уровень сжатия: '))
        for i in list_file('png', 'jpg', 'gif'):
            if i[0] == n:
                Image.open(i[1]).save(i[1], quality=quality)
                return 'Успех'
    else:
        return


def delite_file_menu():  # 4
    c_fanc = menu()
    if c_fanc == 1:
        print(del_start())
    elif c_fanc == 2:
        print(del_end())
    elif c_fanc == 3:
        print(del_middle())
    elif c_fanc == 4:
        print(del_extension())
    else:
        print(del_file())


def delite_file():
    for i in list_file(''):
        print(*i)


def del_start():
    delite_file()
    contecst = input('Введите подстроку: ')
    for i in list_file(''):
        if i[1].startswith(contecst):
            os.remove(i[1])
    return 'Успех'


def del_end():
    delite_file()
    contecst = input('Введите подстроку: ')
    if contecst != '0':
        for i in list_file(''):
            name_file = i[1].split('.')
            if name_file[0].endswith(contecst):
                os.remove(i[1])
            return 'Успех'
    else:
        return
        # pattern = fr'({contecst})(?:\.\w+)'
        # match = re.findall(pattern, ' '.join(i for i in sp_pattern)


def del_middle():
    delite_file()
    contecst = input()
    if contecst != '0':
        for i in list_file(''):
            if contecst in i[1]:
                os.remove(i[1])
        return 'Успех'
    else:
        return


def del_extension():
    delite_file()
    extension = input('Введите расширение: ')
    if extension != '0':
        for i in list_file(''):
            if i[1].endswith(extension):
                os.remove(i[1])
        return 'Успех'
    else:
        return


def del_file():
    delite_file()
    n = int(input('Выберите файл: '))
    if n != 0:
        for i in list_file(''):
            if i[0] == n:
                os.remove(i[1])
                return 'Успех'
    else:
        return