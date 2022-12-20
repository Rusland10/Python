def read_file(name) -> list:
    with open(name, 'r') as rf:
        words = rf.read().split()
    for i in range(len(words)):
        words[i] = words[i].lower()
        words[i] = ''.join(j for j in words[i] if j.isalpha())
    for word in words:
        if word == '' or len(word) == 1:
            words.remove(word)
    words = set(words)
    return list(words)def save_file(name: str, words: list) -> None:
    words = sorted(words)
    with open('outread_.txt', 'w') as sf:
        sf.write(f'Количество уникальных слов: {str(len(words))}\n')
        sf.write('\n'.join(words))
save_file('outread.txt', read_file('read_file.txt'))