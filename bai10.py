# Bài 10: Cho số nguyên dương n. Kiểm tra xem n có phải là số nguyên tố hay không
import math
from utils import massive_input

def is_prime_number(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_number_extend(n: int) -> bool:
    if n < 2:
        return False

    limit = int(math.sqrt(n)) + 1

    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

input_n = 7
print(is_prime_number(input_n))

inputs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(massive_input(inputs, is_prime_number))
print(massive_input(inputs, is_prime_number_extend))
