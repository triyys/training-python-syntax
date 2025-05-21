# Bài 8: Tìm ước số lẻ lớn nhất của số nguyên dương n

def greatest_odd_divisor(n: int) -> int:
    # Reverse range from n to 2
    for i in range(n, 0, -1):
        if n % i == 0 and i % 2 == 1:
            return i
    return -1

def greatest_odd_divisor_extend(n: int) -> int:
    if n % 2 == 1:
        return n

    # Reverse range from n to 2
    for i in range(n, 0, -1):
        if n % i == 0 and i % 2 == 1:
            return i
    return -1

input_n = 8
print(greatest_odd_divisor(input_n))
print(greatest_odd_divisor_extend(input_n))

