# 6. (МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4


nums = input('Введите элементы 1-го списка:')
nums1 = nums.split(',')
nums = input('Введите элементы 2-го списка:')
nums2 = nums.split(',')

for num2 in nums2:
    if num2 in nums1:
        nums1.remove(num2)
print(','.join(nums1))