# Bài 7: Tính tích tất cả các “ước số chẵn” của số nguyên dương n

def product_even_divisor(n: int) -> int:
    result = 1

    for i in range(2, n + 1, 2):
        if n % i == 0:
            result *= i

    return result

input_n = 12
print(product_even_divisor(input_n))
