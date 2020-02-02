# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import  count, cycle

for el in count(7):
    if el > 15:
        break
    else:
        print(el)


с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1