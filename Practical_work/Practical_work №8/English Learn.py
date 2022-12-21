import pymorphy2
import re
from translate import Translator
with open(r"C:\Users\Руслан\Downloads\Telegram Desktop\dialog-681583815.html", encoding='utf8') as f:
    rez = f.read()
pattern = r'(?:class=\"msg-body\">)([^<+]+)(?:</p>)'
match = re.findall(pattern, rez)
slov = []
slovar = {}
for i in range(len(match)):
    slov.extend(match[i].split())
morfi = pymorphy2.MorphAnalyzer()
norm = [morfi.parse(i)[0].normal_form for i in slov]
for i in norm:
    if i in slovar:
        continue
    elif i not in slovar:
        slovar[i] = norm.count(i)
slovar = dict(sorted(slovar.items(), key=lambda item: item[1], reverse=True))
print(slovar)
trnsl = []
translates = Translator(from_lang='ru', to_lang='English')
# print(translates.translate())
for i in slovar.keys():
    trnsl.append(translates.translate(i))
print(trnsl)