# Bài 4: Tính S(n) = 1 + x^2/2! + x^4/4! + … + (x^2n)/(2n)!

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sum_equation(n: int, x: int) -> int:
    if n == 0:
        return 1

    result = 1

    for i in range(1, n + 1):
        equation_result = x ** (i * 2) / factorial(i * 2)
        result += equation_result

    return result

input_n = 12
input_x = 2
print(sum_equation(input_n, input_x))
