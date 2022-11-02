stroka = input()

print(stroka[2])
print(stroka[len(stroka) - 1])

for i in range(0, 5):
    print(stroka[i], end='')

print('\n')

for i in range(0, len(str) - 2):
    print(str[i], end='')

print('\n')

string_chet = ''
string_nechet = ''
for i in range(0, len(str)):
    if i % 2 == 0:
        string_chet += str[i]
    else:
        string_nechet += str[i]

print(string_chet)
print(string_nechet)

print(str[::-1])
print(str[::-2])