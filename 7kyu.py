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

def DNA_strand(dna: str) -> str:
    """
    Функция для изменния строки по заданным параметрам
    :param dna: исходная строка
    :return: измененая строка
    """
    dnk = {'A': 'T',
           'T': 'A',
           'C': 'G',
           'G': 'C', }
    return ''.join((dnk[word] for word in dna))


assert DNA_strand("AAAA") == "TTTT"
