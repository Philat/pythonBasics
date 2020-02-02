# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

from random import randint

my_list = [el*randint(0,30) for el in range(10, 20)]
print(my_list)
new_list =[]
for i in range(0,len(my_list)-1):
    if my_list[i]<my_list[i+1]:
        new_list.append(my_list[i+1])

print(new_list)