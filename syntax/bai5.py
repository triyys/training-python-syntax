# Bài 5: Đếm số lượng “ước số lẻ” của số nguyên dương n

def odd_divisor_count(n: int) -> int:
    result = 1

    for i in range(3, n + 1, 2):
        if n % i == 0:
            result += 1

    # Tách dòng ra.
    return result

input_n = 9
print(odd_divisor_count(input_n))
