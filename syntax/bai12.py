# Bài 12: Hãy tính tổng các chữ số của số nguyên dương n

# Tốt.
# Thử sử dụng hàm divmod 
def sum_digit(n: int) -> int:
    result = 0

    while n > 0:
        result += n % 10
        n = n // 10

    return result

input_n = 25
print(sum_digit(input_n))

