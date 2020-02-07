# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

flag = ' '
def inputFunc():
    new_string = input("Введите строку:" )
    global flag
    flag = new_string

while flag!='':
    inputFunc()
    f = open('task1.txt', 'a')
    f.writelines('\n'+flag)
    f.close()