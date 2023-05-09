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
