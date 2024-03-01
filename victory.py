def victorina(names):
    while True:
        years = [1971, 1971, 1984, 1985, 1956]
        correct = 0
        incorrect = 0
        for i in range(len(names)):
            print('Когда родился', names[i], '? ')
            ask = int(input())
            if ask == years[i]:
                correct += 1
            else:
                incorrect += 1

        correct_perc = (correct * 100)/5
        incorrect_perc = (incorrect * 100)/5

        print('Правильных ответов:', correct)
        print('Неправильных ответов:', incorrect)
        print('Процент верных ответов:', correct_perc)
        print('Процент неверных ответов:', incorrect_perc)

        main_answer = str(input('Вы хотите начать заново? Да/Нет '))
        if main_answer == 'Да':
            continue
        else:
            break


names1 = ["Тупак", "Маск", "Цукерберг", "Альтман", "Россум"]
victorina(names1)
