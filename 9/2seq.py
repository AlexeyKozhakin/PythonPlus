# (МОДУЛЬ 2) создать модуль 2seq.py. Задание:
# Пользователь вводит любые цифры через запятую
# Сохранить цифры в список
# Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
# Вывести новый список на экран
# Порядок цифр в новом списке не важен
# Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
# Результат: 2, 4, 6, 9

nums = input('Введите элементы списка через запятую:')
nums = nums.split(',')
nums_uniqe=[]
for i in range(len(nums)):
    if nums[i] not in nums[:i]+nums[i+1:]:
        nums_uniqe.append(nums[i])
print(', '.join(nums_uniqe))