# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

def rec(x):
    sum = 0
    while x >= 0:
        sum = sum + ((-1)**(x+1))*(1 / (2 ** x))
        x = x - 1
        rec(x)
    return  -sum

# 1000 loops, best of 5: 1.53 msec per loop func - 10
# 1000 loops, best of 5: 46.8 msec per loop  func - 15
# для аргумента 100 компьютер завис

def rec2(x):
    my_list = [1/(2**el)*(1 if el%2==0 else -1) for el in range(0,x)]
    new_sum = sum(my_list)
    return new_sum

#1000 loops, best of 5: 4.64 usec per loop func - 10
#1000 loops, best of 5: 6.93 usec per loop func - 15
#1000 loops, best of 5: 58.5 usec per loop func - 100


def rec3(x):
    new_sum =0
    for el in range(0,10):
        new_sum=new_sum+(1/(2**el)*(1 if el%2==0 else -1))
    return new_sum

# 1000 loops, best of 5: 4.22 usec per loop func - 10
# 1000 loops, best of 5: 4.37 usec per loop func - 15
# 1000 loops, best of 5: 4.32 usec per loop func - 100

