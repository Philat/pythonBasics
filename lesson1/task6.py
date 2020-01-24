# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.


start = float(input("Введите начальный показатель спорстмена: "))
finish = float(input("Введите целевой показатель спорстмена: "))
progress_final = 0
i=0
while progress_final < finish:
    progress_final = round(start*(1.1**i),2)
    print(f'{i+1} День: {progress_final}')
    i = i+1

print(f"Ответ: на {i}-й день: спортсмен достиг результата — не менее {finish} км")