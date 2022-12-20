number = int(input())
number_str = str(number)
if int(number_str[2]) > int(number_str[1]) > int(number_str[0]):
    print('Да')
else:
    print('Нет')