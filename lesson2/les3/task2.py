# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

list_1 = [1,2,3,4,5,2,1,2,3,4,2,1,3,43,2,4,3,2,3,5,6,45]
list_2 = []
for k, i in enumerate(list_1):
    if i%2 ==0:
        list_2.append(k)
print(list_2)