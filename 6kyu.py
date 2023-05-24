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

# # 6 kyu Sums of Parts
# def parts_sums(ls: List[int]) -> List[int]:
#     result = []
#     total_sum = sum(ls)
#     for value in ls:
#         result.append(total_sum)
#         total_sum -= value
#     result.append(0)
#     return result
#
#
# assert parts_sums([0, 1, 3, 6, 10]) == [20, 20, 19, 16, 10, 0]

# 6 кю Преобразование строки в верблюжий регистр
# def to_camel_case(text: str):
#     text = text.replace('-', ' ')
#     text = text.replace('_', ' ')
#     if text.strip() != '':
#         result = text.split()[0]
#         return result + ''.join((word.capitalize() for word in text.split()[1:]))
#     return text

# 6 кю Сортировать лишнее
def sort_array(source_array: list) -> list:
    odds = sorted([n for n in source_array if n % 2 != 0])
    for i, n in enumerate(source_array):
        if n % 2 != 0:
            source_array[i] = odds.pop(0)
    return source_array


# 6 кю Дублирующий кодер

# def duplicate_encode(word: str):
#     word = word.lower()
#     return ''.join([')'
#                     if word.count(i) > 1
#                     else '('
#                     for i in word])

