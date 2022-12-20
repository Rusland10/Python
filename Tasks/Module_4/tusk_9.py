number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 == number2 and number2 == number3:
    print(3)
elif number1 == number2 or number2 == number3 or number1 == number3:
    print(2)
else:
    print(0)