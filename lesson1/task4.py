# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

m = input("Введите число: ")
my_list = list(m)
result = [int(item) for item in my_list]
i = 9
counter = 0

while i >= 0:
    if i>counter:
        for el in result:
            if i == el:
                counter=el
    i=i-1

print(counter)