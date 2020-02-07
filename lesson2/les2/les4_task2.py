def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


# 1000 loops, best of 5: 2.87 usec per loop
# 1000 loops, best of 5: 4.14 usec per loop
# 1000 loops, best of 5: 19 usec per loop
# 1000 loops, best of 5: 203 usec per loop


def func(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    #print(*list(filter(lambda x: x != 0, numbers)))

# 1000 loops, best of 5: 2.92 usec per loop
# 1000 loops, best of 5: 3.98 usec per loop
# 1000 loops, best of 5: 20 usec per loop
# 1000 loops, best of 5: 242 usec per loop
