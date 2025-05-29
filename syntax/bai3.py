# Bài 3: Tính S(n) = x + x^2 + x^3 + … + x^n

# Làm phức tạp quá, gọi pow là được
def sum_exponential(n: int, x: int) -> int:
    if n == 0:
        return 1

    cache = x ** 0
    result = 0
    for i in range(1, n + 1):
        cache = cache * x
        result += cache
    return result

def sum_exponential_o1(n: int, x: int) -> int:
    if n == 0:
        return 1

    return int(x * (x ** n - 1) / (x - 1))

input_n = 4
input_x = 2
print(sum_exponential(input_n, input_x))
print(sum_exponential_o1(input_n, input_x))
