def my_func(user_inp):
    if user_inp == 1799:
        ask = int(input('А какой день? '))
        if ask == 6:
            print('Верно!')
        else:
            print('Неверно!')
    else:
        print('Неверный год рождения!')

my_func(int(input('Какой год рождения у Пушкина? ')))