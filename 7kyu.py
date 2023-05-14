# def solution(text: str, ending: str) -> bool:
#     """
#     Функция для проверки  заканчивается ли первая строка вторым аргументом (тоже строкой).
#     :param text: первая строка
#     :param ending: второая строка
#     :return: булевое значение взависимости от результата
#     """
#     if text.endswith(ending):
#         return True
#     return False
#
#
#
# assert solution('abc', 'bc') == True
# assert solution('abc', 'd') == False
from functools import reduce

from typing import Optional, Union


# def DNA_strand(dna: str) -> str:
#     """
#     Функция для изменния строки по заданным параметрам
#     :param dna: исходная строка
#     :return: измененая строка
#     """
#     dnk = {'A': 'T',
#            'T': 'A',
#            'C': 'G',
#            'G': 'C', }
#     return ''.join((dnk[word] for word in dna))

# 7 кю В порядке убывания
# def descending_order(num: int) -> int:
#     # Bust a move right here
#     return int(''.join(sorted(str(abs(num)), reverse=True)))

# 7 кю Помогите Судзуки сосчитать овощи....
# def count_vegetables(string: str) -> list: vegetables = ("cabbage",
# "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip") result = [(string.count(
# vegetable), vegetable) for vegetable in vegetables] return sorted(result, key=lambda x: (x[0], x[1]), reverse=True)


