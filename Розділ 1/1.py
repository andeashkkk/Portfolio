import re
print('Страп Андріана група 2 варіант 15 лабораторна 1')
s = str(input('Enter text: '))
x = s.strip(' ')
print(x)
print(x + ' horse')
r = re.sub(r"[^0-9]", '', s)
print(r)
dic = {'а':'a', 'б':'b', 'в':'v', 'г':'h', 'ґ':'g', 'д':'d', 'е':'e', 'є':'je', 'ж':'zh', 'з':'z', 'и':'i',
       'і':'y', 'ї':'ji', 'й':'ij', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'о', 'п':'p', 'р':'r', 'с':'s',
       'т':'t', 'у':'u', 'ф':'f', 'х':'ch', 'ц':'ts','ш':'sj', 'щ':'sch', 'ь':'', 'ю':'uu', 'я':'ja'}
st = str(input('Enter text: '))
result = str()
for i in st:
    result += dic.get(i.lower(), i.lower()).upper() if i.isupper() else dic.get(i, i)
print(result)