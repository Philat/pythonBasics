# 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def division(a,b):
    return a/b if b !=0 else print('Деление на ноль невозможно')

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

print(f'Частное:{ round(division(a,b),2)}') if b!=0 else print('Деление не выполнено')