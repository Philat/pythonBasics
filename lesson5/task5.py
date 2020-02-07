# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

new_string = input("Введите строку из чисел разделенных пробелами:" )

f = open('task5.txt', 'w')
f.writelines(new_string)
f.close()

f = open('task5.txt', 'r')
content = f.read().split()
f.close()

content = list(map(int, content))
print(sum(content))