# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f = open('task4.txt', 'r')
content = f.readlines()
f.close()
translate = {'One': 'Один', 'Two':'Два', 'Three':'Три', 'Four': 'Четыре'}
new_content = []
for el in content:
    el = el.split(' — ')
    new_content.append(translate[el[0]]+' - '+el[1])
f = open('task4_2.txt','w')
f.writelines(new_content)
f.close()