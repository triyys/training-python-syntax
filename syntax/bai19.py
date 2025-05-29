# Bài 19: Hãy kiểm tra các chữ số của số nguyên dương n có tăng dần từ trái sang phải hay không

# Tách dòng ra
def is_asc_digits(n: int) -> bool:
    previous_remainder = 10
    while n > 0:
        remainder = n % 10

        if remainder > previous_remainder:
            return False

        previous_remainder = remainder

        n //= 10

    return True

input_n = 1235666
print(is_asc_digits(input_n))
