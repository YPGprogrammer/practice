def my_func(year):
    while True:
        user_input = int(input('Какой год рождения у Пушкина? '))
        if user_input != year:
            print('Неверно!')
            continue
        else:
            print('Верно!')
            break

my_func(1799)