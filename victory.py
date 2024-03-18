#Гагарин        1934
#Ломоносов      1711
#Ньютон         1643
#Эйнштейн       1879
#Декарт         1596
dic={
'Гагарин': 1934,
'Ломоносов': 1711,
'Ньютон': 1643,
'Эйнштейн': 1879,
'Декарт': 1596
}
ct=0
cf=0
# year_GAGARIN = 1934
# year_Lomonosov = 1711
# year_Newton = 1643
# year_Einstain = 1879
# year_Cartesius = 1596
print('Добро пожаловать в векторину угадай год рождения знаменитости:')
for name in dic.keys():
    while True:
        year = int(input(f'Назовите год рождения {name}:'))
        if year == dic[name]:
            print('Верно!')
            ct+=1
            break
        else:
            print('Неверно')
            cf+=1

print(f'Процент угадывания:{round(ct/(cf+ct)*100)}%')