# Bài 1: Tính S(n) = 1 + 2 + 3 + … + n

# O(n)
def sum_n(n: int) -> int:
    result = 0
    for i in range(n + 1):
        result += i
    return result

# O(1)
def sum_1(n: int) -> int:
    return int(n * (n + 1) / 2)

input_n = 2
print(sum_n(input_n))
print(sum_1(input_n))
