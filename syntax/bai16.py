# Bài 16: Tìm chữ số nhỏ nhất của số nguyên dương n

# Tốt
def min_digit(n: int) -> int:
    result = 10

    while n > 0:
        n, remainder = divmod(n, 10)
        result = min(result, remainder)

    return result

input_n = 6988885
print(min_digit(input_n))
