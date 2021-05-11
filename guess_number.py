"Тестирование функции"

def game_core_v4(number):
    '''Введём в функцию две вспомогательные переменные n и m и будем брать число из середины диапазона
       от n до m и уменьшать этот диапазон опять вдвое'''
    count = 1
    n = 0
    m = 101
    predict = 50
    while number != predict:
        count += 1
        if number > predict:
            n = predict  # Уменьшаем диапазон со стороны "n", до выбранного в предыдущей попытке
            if m - n == 2:
                predict = (n + m)//2
                print(predict)
                break
            if (m - n) % 2 == 1:  # Проверяем делится ли на 2 ровно или нет
                predict = n + (m - n)//2 + 1    # Если нет, то прибавляем 1
                print(predict)
            else:
                predict = n + (m - n)//2
                print(predict)
        elif number < predict:
            m = predict  # Уменьшаем диапазон со стороны "m", до выбранного в предыдущей попытке
            if m - n == 2:
                predict = (n + m)//2
                print(predict)
                break
            if (m - n) % 2 == 1:
                predict = n + (m - n)//2 + 1
                print(predict)
            else:
                predict = n + (m - n)//2
                print(predict)
    return(count) # выход из цикла, если угадали

# score_game(game_core_v4)

print(game_core_v4(80))