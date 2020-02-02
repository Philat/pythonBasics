# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum(a,b,c):
    new_list = [a,b,c]
    new_list.sort(reverse = True )
    return new_list[0]+new_list[1]

print(sum(12,6,10))