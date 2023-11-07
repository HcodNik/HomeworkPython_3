import random
from random import sample
'''
7. (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими
библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока
использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде:
третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
'''
birtday = {
    'Александр Пушкин': '06.06.1799',
    'Альберт Эйнштейн': '14.03.1879',
    'Никола Тесла': '10.07.1856',
    'Алан Тьюринг': '23.06.1912',
    'Стив Джобс': '24.02.1955',
    'Джефф Безос': '12.01.1964',
    'Билл Гейтс': '28.10.1955',
    'Уоррен Баффет': '30.08.1930',
    'Владимир Путин': '07.10.1952',
    'Джозеф Байден-младший': '20.11.1942',
}

quest_items = random.sample(list(birtday.items()), 5)
print(quest_items)
for i in range(len(quest_items)):
    quest_user = input(f'{''.join(quest_items[i][0])} - укажите дату рождения в формате dd.mm.yyyy: ')
    if quest_items[i][1] == quest_user:
        print('Правильный ответ!')



# quest = input(f'Укажите дату рождения {random.sample(birtday.keys(),1)}')



'''
birth_Pushkin = int(input("Укажите дату рождения Александра Пушкина: ")) # 06.06.1799
birth_Einstein = int(input("Укажите дату рождения Альберта Эйнштейна: ")) # 1879
birth_Tesla = int(input("Укажите дату рождения Николы Тесла: ")) # 1856
birth_Jobs = int(input("Укажите дату рождения Стива Джобса: ")) # 1955
birth_Turing = int(input("Укажите дату рождения Алана Тьюринга: ")) # 1912
catch0 = 0 # счётчик правильных ответов
catch1 = 0 # счётчик неправильных ответов

if yearPushkin == 1799:
    catch0 += 1
else:
    catch1 += 1
if yearEinstein == 1879:
    catch0 += 1
else:
    catch1 += 1
if yearTesla == 1856:
    catch0 += 1
else:
    catch1 += 1
if yearJobs == 1955:
    catch0 += 1
else:
    catch1 += 1
if yearTuring == 1912:
    catch0 += 1
else:
    catch1 += 1

print("Кол-во правильных ответов:", catch0)
print("Кол-во ошибок:", catch1)
print("Процент правильных ответов:", catch0*100/5)
print("Процент неправильных ответов:", catch1*100/5)
'''
