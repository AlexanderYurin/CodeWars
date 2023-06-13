from typing import Dict


# 5 kyu Pete, the baker
# def cakes(recipe: Dict, available: Dict) -> int:
#     """
#     Эта функция для рассчета кол-ва приготовленных блюд
#     :param recipe рецепт
#     :param available продукты
#     :return сколько можно приготовить блюд
#     """
#     for ingredient in recipe:
#         if ingredient not in available:
#             return 0
#
#     return min(available[ingredient] // recipe[ingredient] for ingredient in recipe)

# # 5 kyu Simple Fun #81: Digits Product
# def digits_product(product: int) -> int:
#     if product < 10:
#         return 10 + product
#     factors = []
#     for i in range(9, 1, -1):
#         while product % i == 0:
#             factors.append(i)
#             product //= i
#     if product > 1:
#         return -1
#     else:
#         return int(''.join(map(str, reversed(factors))))

# # 5 кю  Не очень безопасно
#
# def alphanumeric(password: str) -> bool:
#     return password.isalnum()

# 5 kyu flatten()

# def flatten(*args) -> list:
#     new_array = []
#     for item in args:
#         if isinstance(item, list):
#             new_array += flatten(*item)
#         else:
#             new_array.append(item)
#     return new_array
#
# assert flatten([1, [3], [[2]]]) == [1, 3, 2]

# 5 kyu Best travel

# def choose_best_sum(t, k, ls):
#     from itertools import combinations
#     try:
#         sum_all_mil = max((mil for mil in map(sum, combinations(ls, k)) if mil <= t))
#     except ValueError:
#         return None
#     else:
#         return sum_all_mil
# def last_digit(n1, n2):
#     return pow(n1, n2, 10)
