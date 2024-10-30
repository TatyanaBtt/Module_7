#  Использование %:
team1_num = int(input('Введите количество участников команды "Мастера кода": '))
team2_num = int(input('Введите количество участников команды "Волшебники данных": '))
print('В команде Мастера кода участников: %s!' % team1_num)
print('В команде Волшебники данных участников: %s!' % team2_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))


#  Использование format():
score_1 = int(input('Введите количество решенных задач команды 1: '))
score_2 = int(input('Введите количество решенных задач команды 2: '))
print('Команда Мастера кода решила задач: {} !'.format(score_1))
print('Команда Волшебники данных решила задач: {} !'.format(score_2))


team1_time = float(input('Введите время, за которое команда "Мастера кода", решила задачи: '))
team2_time = float(input('Введите время, за которое команда "Волшебники данных", решила задачи: '))
print('Мастера кода решили задачи за {} секунд!'.format(team1_time))
print('Волшебники данных решили задачи за {} секунд!'.format(team2_time))


# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')

def challenge_result():
    global score_1
    global score_2
    global team1_time
    global team2_time
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды "Мастера кода"!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды "Волшебники данных"!'
    else:
        result = 'Ничья!'
    print(result)


challenge_result()

tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 2)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
