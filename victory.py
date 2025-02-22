'''
7. (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова

1 июня - Михаил Глинка, композитор, 1804 год.
3 июня - Елена Исимбаева, легкоатлетка, 1982 год.
4 июня - Виктор Тихонов, тренер по хоккею, 1930 год.
5 июня - Александр Невский, полководец, 1220 год.
6 июня - Александр Сергеевич Пушкин, поэт, 1799 год.
9 июня - Петр I, император, 1672 год.
10 июня - Илья Глазунов, живописец, 1930 год.
10 июня - Людмила Зыкина, певица, 1929 год.
11 июня - Олег Видов, актер, 1946 год.
18 июня - Юрий Соломин, актер, 1935 год.
18 июня - Иван Гончаров, писатель, 1812 год.
21 июня - Александр Твардовский, поэт, 1910 год.
22 июня - Наталья Варлей, актриса, 1947 год.
23 июня - Анна Ахматова, поэтесса, 1889 год
'''
import random
numbers = list(range(10))

is_vict_over = False
total_answer = 5
questions = [
    ['Михаил Глинка, композитор', '01.06.1804',  'первое июня 1804 года'],
    ['Елена Исимбаева, легкоатлетка', '03.06.1982', 'третье июня 1982 года'],
    ['Виктор Тихонов, тренер по хоккею', '04.06.1930', 'четвёртое июня 1930 года'],
    ['Александр Невский, полководец', '05.06.1220', 'пятое июня 1930 года'],
    ['Александр Сергеевич Пушкин, поэт', '06.06.1799', 'шестое июня 1799 года'],
    ['Петр I, император', '09.06.1672', 'девятое июня 1672 года'],
    ['Илья Глазунов, живописец', '10.06.1930', 'десятое июня 1930 года'],
    ['Людмила Зыкина, певица', '10.06.1929', 'десятое июня 1929 года'],
    ['Олег Видов, актер', '11.06.1946', 'одинадцатое июня 1946 года'],
    ['Юрий Соломин, актер', '18.06.1935', 'восемнадцатое июня 1935 года']
]

while not is_vict_over:
    print('Предлагаю сыграть в викторину')
    print('Вам будет предложено', total_answer, 'вопросов о днях рождения')
    print("Вводите дату в формате 'dd.mm.yyyy'")
    correct_answer = 0
    result = random.sample(numbers, 5)

    for i in range(total_answer):
        que = questions[result[i]]
        print(f'Вопрос №{i + 1}')
        answer = input(f'Когда год рожденья у {que[0]}?')
        if answer == que[1]:
            correct_answer += 1
        else:
            print('Ошибка.\nВерный ответ:', que[2])

    print('количество правильных ответов:', correct_answer)
    print('количество ошибок:', total_answer - correct_answer)
    print('процент правильных ответов', correct_answer * 100 / total_answer)
    print('процент неправильных ответов', (total_answer - correct_answer) * 100 / total_answer)

    answer = input('Начать игру сначала?')
    if answer != 'да' and answer != 'yes' and  answer != 'Да' and answer != 'Yes':
        is_vict_over = True
