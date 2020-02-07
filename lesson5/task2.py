# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f = open('task2.txt', 'r')
content = f.read()
f.close()

content = content.split('\n')
print(f'Количество строк: {len(content)}')
for i, el in enumerate(content):
    print(f'Количество слов в строке {i+1}: {len(el.split())}')