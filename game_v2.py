import numpy as np

def game_core_v2(number: int = 1) -> int:
    """Угадываем число бинарным поиском

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while low <= high:
        count += 1
        mid = (low + high) // 2
        if mid == number:
            break
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1
    return count

def score_game(game_core_v2) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v2 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core_v2(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    score_game(game_core_v2)