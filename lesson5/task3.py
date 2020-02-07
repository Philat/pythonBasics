# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

f = open('task3.txt', 'r')
content = f.readlines()
f.close()
empl = {}

for el in content:
    el_list = el.split()
    empl[el_list[0]]=int(el_list[1])

empl_low = dict(filter(lambda elem: elem[1] < 20000, empl.items()))
print(empl_low.keys())

count = 0
sum = 0
for key in empl:
    count += 1
    sum += empl[key]

print('Среднее: ', sum/count)