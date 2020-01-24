# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

def formater(m):
    array_of_time = []
    array_of_time.append(m)
    sum_array_of_time = array_of_time[0]
    for i in range(1,3):
        array_of_time.append(m*(10**i)+array_of_time[i-1])
        sum_array_of_time = sum_array_of_time + array_of_time[i]
    array_of_time.append(sum_array_of_time)
    return array_of_time

m = int(input("Введите число: "))
array_of_time = formater(m)
print(f'{array_of_time[0]}+{array_of_time[1]}+{array_of_time[2]}={array_of_time[3]}')