year = int(input('Введите год рождения А.С. Пушкина:'))
year_true = 1799
month_true = 'июнь'
day_true = 6
if year == year_true:
    month = input('Введите месяц в котором родился А.С. Пушкина:')
    if month == month_true:
        day = int(input('Введите день в который родился А.С. Пушкина:'))
        if day == day_true:
            print('Верно')
        else:
            print('Неверный день')
    else:
        print('Неверный месяц')
else:
    print('Неверный год')