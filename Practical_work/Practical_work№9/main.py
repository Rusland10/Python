from fanc_s import *


def start():
    while True:
        menu = ['0. Сменить рабочий каталог', '1. Преобразовать PDF в Docx', '2. Преобразовать Docx в PDF',
                '3. Произвести сжатие изображения', '4. Удалить группу файлов', '5. Выход']
        list_command = range(6)
        start_dir = start_directory()
        print(start_dir, "Выберите действие:\n", *menu, sep='\n')
        input_user = int(input('Ваш выбор: '))
        while input_user not in list_command:
            input_user = int(input())
        if input_user == 0:
            print(directory())
        elif input_user == 1:
            print(p2d())
        elif input_user == 2:
            print(d2p())
        elif input_user == 3:
            print(compression())
        elif input_user == 4:
            delite_file_menu()
        else:
            return 'Досвидания'


print(start())