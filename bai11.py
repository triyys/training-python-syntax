# Bài 11: Cho số nguyên dương n. Kiểm tra xem n có phải là số chính phương hay không
import math
from utils import massive_input

def is_square_number(n: int) -> bool:
    # https://www.w3schools.com/python/ref_math_isqrt.asp
    return math.isqrt(n) ** 2 == n

input_n = 17
print(is_square_number(input_n))

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(massive_input(inputs, is_square_number))
