# Bài 17: Hãy kiểm tra số nguyên dương n có toàn chữ số lẻ hay không

# Tách dòng ra
def is_all_odd_digits(n: int) -> bool:
    while n > 0:
        if n % 2 == 0:
            return False
        n //= 10
    return True

input_n = 3933392
print(is_all_odd_digits(input_n))
