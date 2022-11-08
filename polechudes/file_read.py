text = open("slova.txt", encoding="utf-8")
text = text.read()
print(*text.title().split('\n'))


