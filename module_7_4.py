team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
else:
    challenge_result = 'Ничья!'

#Использование %:

print('В команде %(name)s участников: %(team1_num)s!' % {'name': 'Мастера кода', 'team1_num': 5})

print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})


#Использование format():

print('Команда {name} решили задач: {score_2}!' .format(name='Волшебники данных', score_2=42))

print('{name} решили задачи за {team1_time} с!'.format(name='Волшебники данных', team1_time=18015.2))


#Использование f-строк:

print(f'Команды решили {score_1} и {score_2} задач.')

print(f'Результат битвы: {challenge_result}')

print(f'Сегодня было решено: {tasks_total} задач, в среднем по: {time_avg}, секунды на задачу.')




