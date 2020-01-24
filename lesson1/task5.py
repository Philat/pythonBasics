# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.

gross = float(input("Введите значение выручки: "))
costs = float(input("Введите значение издержек: "))

if gross>costs:
    profit = gross-costs
    margin = round(profit/gross,2)
    print('Ваша фирма отработала с прибылью')
    empl = int(input("Введите численность сотрудников: "))
    profit_per_capita = round(profit / empl)
    print(f'\nВаша прибыль составила {profit}.'
          f'\nРентабельность - {margin*100}%.\nПрибыль в расчете на сотрудника - {profit_per_capita}.')
else:
    print(f'Ваша фирма отработала в убыток')