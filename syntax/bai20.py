# Bài 20: Hãy kiểm tra các chữ số của số nguyên dương n có giảm dần từ trái sang phải hay không

def is_desc_digits(n: int) -> bool:
    previous_remainder = 0
    while n > 0:
        remainder = n % 10

        if remainder < previous_remainder:
            return False

        previous_remainder = remainder

        n //= 10

    return True

input_n = 66652211
print(is_desc_digits(input_n))
