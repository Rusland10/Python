def otk():
    f = open('data')
    a = f.readline()
    num_list = f.read().splitlines()
    num_list = [int(i) for i in num_list]

    return num_list

print(otk())