# def century(year: int) -> int:
#     if year % 100 == 0:
#         return year // 100
#     return year // 100 + 1


# def remainder(a, b):
#     try:
#         nums = (a, b)
#         result = max(nums) % min(nums)
#         if result == 0 and min(nums) > 0 and max(nums) == 0 or min(nums) == 0:
#             raise ZeroDivisionError
#     except ZeroDivisionError:
#         return None
#     else:
#         return result
#
#
# assert remainder(1, 0) is None
# assert remainder(0, -1) == 0
# assert remainder(17, 5) == 2
# assert remainder(13, 72) == 7
# 8 кю Квадрат(n) Сумма
# def square_sum(numbers):
#     return sum(map(lambda x: x**2, numbers))
#  8 кю Транспорт в отпуске
# def rental_car_cost(d):
#     total_cost_no_sale = d * 40
#     if d >= 7:
#         return total_cost_no_sale - 50
#     elif d >= 3:
#         return total_cost_no_sale - 50
#     return total_cost_no_sale

