# 2. В проекте реализовать следующий функционал:
# После запуска программы пользователь видит меню, состоящее из следующих пунктов:
# - создать папку;
# - удалить (файл/папку);
# - копировать (файл/папку);
# - просмотр содержимого рабочей директории;
# - посмотреть только папки;
# - посмотреть только файлы;
# - просмотр информации об операционной системе;
# - создатель программы;
# - играть в викторину;
# - мой банковский счет;
# - смена рабочей директории (*необязательный пункт);
# - выход.
# Так же можно добавить любой дополнительный функционал по желанию.
 
# Описание пунктов:
# - создать папку
# после выбора пользователь вводит название папки, создаем её в рабочей директории;
# - удалить (файл/папку)
# после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
# - копировать (файл/папку)
# после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
# - просмотр содержимого рабочей директории
# вывод всех объектов в рабочей папке;
# - посмотреть только папки
# вывод только папок которые находятся в рабочей папке;
# - посмотреть только файлы
# вывод только файлов которые находятся в рабочей папке;
# - просмотр информации об операционной системе
# вывести информацию об операционной системе (можно использовать пример из 1-го урока);
# - создатель программы
# вывод информации о создателе программы;
# - играть в викторину
# запуск игры викторина из предыдущего дз;
# - мой банковский счет
# запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать);
# - смена рабочей директории (*необязательный пункт)
# усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней;
# - выход
# выход из программы.
# Так же можно добавить любой другой интересный или полезный функционал по своему желанию
# После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
# 3. Выложите проект на github:
# 4. Можно сдать задание в виде pull request:
# 5. Посмотреть разбор дз по функциям, если требуется, то сделать работу надо ошибками.1. Создать новый проект ""Консольный файловый менеджер"

import os
import shutil
import platform
import subprocess


def menu():
    print('1.  - создать папку')
    print('2.  - удалить (файл/папку)')
    print('3.  - копировать (файл/папку)')
    print('4.  - просмотр содержимого рабочей директории')
    print('5.  - посмотреть только папки')
    print('6.  - посмотреть только файлы')
    print('7.  - просмотр информации об операционной системе') #+
    print('8.  - создатель программы')
    print('9.  - играть в викторину')
    print('10. - мой банковский счет')
    print('11. - смена рабочей директории (*необязательный пункт)')
    print('12. - выход') #+
    choice = input('Выберите действие: ')
    return choice

def create_folder():
    name = input('Введите имя каталога для создания: ')
    os.mkdir(f"./{name}")

def delete_folder():
    name = input('Введите имя каталога для удаление: ')
    os.rmdir(f"./{name}")
    
def copy_folder():
    name = input('Введите имя каталога или файла для копирования: ')
    name_copy = input('Введите имя с которым хотите сохранить: ')
    if os.path.isfile(f'./{name}'):
        # Копирование файла
        shutil.copy(f"./{name}", f"./{name_copy}")
    else:    
        # Копирование папки
        shutil.copytree(f"./{name}", f"./{name_copy}")     
    
def show_folder():
    for folder in os.listdir(r"./"):
        print(folder)
    
def show_folders():
    for folder in os.listdir(r"./"):
        if not os.path.isfile(f'./{folder}'): 
            print(folder)    

def show_files():
    for folder in os.listdir(r"./"):
        if os.path.isfile(f'./{folder}'): 
            print(folder)    
    
def os_info():
    print('Семейство операциной системы:', os.name)
    # Получение имени операционной системы
    os_name = platform.system()
    print("Операционная система:", os_name)

    # Получение версии операционной системы
    os_version = platform.version()
    print("Версия операционной системы:", os_version)

def author_info():
    print('Author: Alexey Kozhakin')
    print('email: alexeykozhakin@yanex.ru')
    
def change_dir():
    name = input('Введите путь директории куда хотите перейти: ')
    os.chdir(name)

    

while True:
    choice = menu()
    if choice == '1':
        create_folder()
    if choice == '2':
        delete_folder()
    if choice == '3':
        copy_folder()
    if choice == '4':
        show_folder()
    if choice == '5':
        show_folders()
    if choice == '6':
        show_files()
    if choice == '7':
        os_info()
    if choice == '8':
        author_info()
    if choice == '9':
        # Запуск программы из соседнего модуля
        subprocess.run(["python", "../9/victori.py"])
    if choice == '10':
        # Запуск программы из соседнего модуля
        subprocess.run(["python", "../10/use_functions.py"])
    if choice == '11':
        change_dir()
    if choice == '12':
        break
        



