"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def algor_predict(number: int = 1) -> int:
    """Угадываем число, предлагая середину диапазона.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    beg_diap = 0
    end_diap = 100

    while True:
        count += 1
        predict_number = round((end_diap-beg_diap)/2 + beg_diap) # предполагаем число - середину диапазона
        
        if predict_number > number:
            end_diap = predict_number

        elif predict_number < number:
            beg_diap = predict_number
    
        else:
            break # выход из цикла, если угадано
    return count


def score_game(algor_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает алгоритм

    Args:
        agor_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 100, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(algor_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(algor_predict)