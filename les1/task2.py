# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

def formater(seconds):
    array_of_time = []
    array_of_time.append(round(seconds//3600))
    array_of_time.append((seconds-array_of_time[0]*3600)//60)
    array_of_time.append(seconds-array_of_time[0]*3600-array_of_time[1]*60)
    return array_of_time



seconds = int(input("Введите количество секунд для форматирования: "))
array_of_time = formater(seconds)
print(f'{array_of_time[0]}:{array_of_time[1]}:{array_of_time[2]}')
