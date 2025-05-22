# Bài 14: Hãy đếm số lượng chữ số của số nguyên dương n

def digit_count(n: int) -> int:
    result = 0
    mutable_n = n

    while mutable_n > 0:
        result += 1
        mutable_n = mutable_n // 10
    return result

input_n = 10
print(digit_count(input_n))
