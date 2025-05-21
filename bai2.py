# Bài 2: Tính S(n) = 1 + 1.2 + 1.2.3 + … + 1.2.3….N
from utils import massive_input

def sum_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    cache = 1
    result = 1
    for i in range(2, n + 1):
        cache = cache * i
        result += cache

    return result

input_n = 2
print(sum_factorial(input_n))

inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(massive_input(inputs, sum_factorial))
