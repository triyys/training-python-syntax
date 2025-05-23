# Bài 15: Tìm chữ số lớn nhất của số nguyên dương n

def max_digit(n: int) -> int:
    mutable_n = n // 10
    result = n % 10

    while mutable_n > 0:
        current_digit = mutable_n % 10
        result = max(result, current_digit)
        mutable_n = mutable_n // 10

    return result

input_n = 168333
print(max_digit(input_n))
