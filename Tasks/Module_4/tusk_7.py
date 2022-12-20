number = int(input())
if number == int(str(number)[::-1]):
    print('Да')
else:
    print('Нет')