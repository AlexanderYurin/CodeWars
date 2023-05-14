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

