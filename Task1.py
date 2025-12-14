money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
current_money = money_capital

# Первый месяц (без роста цен)
if current_money + salary >= spend:
    current_money = current_money + salary - spend
    months += 1

# Последующие месяцы
while current_money + salary >= spend * ((1 + increase) ** months):
    current_money = current_money + salary - spend * ((1 + increase) ** months)
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
