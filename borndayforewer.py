year_true = 1799
day_true = 6
while True:
    year = int(input('Введите год рождения А.С. Пушкина:'))
    if year == year_true:
        while True:
            day = int(input('Введите день в который родился А.С. Пушкина:'))
            if day == day_true:
                print('Верно')
                break
            else:
                print('Неверный день')
        break
    else:
        print('Неверный год')