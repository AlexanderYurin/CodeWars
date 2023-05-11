# 6 kyu Pair of gloves
from typing import List


# def number_of_pairs(gloves: List[str]) -> int:
#     """
#     Эта функция для рассчета пар перчаток
#     :param gloves список перчаток по цветам
#     :return всего кол-во пар перчаток
#     """
#     from collections import Counter
#     return sum((count // 2 for glove, count in Counter(gloves).items()))
#
#
# assert number_of_pairs(["red", "green", "red", "blue", "blue"]) == 2
# assert number_of_pairs(["red", "red", "red", "red", "red", "red"]) == 3
# assert number_of_pairs([]) == 0

# 6 kyu Multiplication table
# def multiplication_table(size: int) -> List[List[int]]:
#     """
#     Функция для создание таблицы умножения в виде списка.
#     :param size: размер таблицы.
#     :return: таблицу ввиде списка.
#     """
#     return [[cal * row for row in range(1, size + 1)] for cal in range(1, size + 1)]
#
#
# assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
