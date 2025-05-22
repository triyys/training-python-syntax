# Bài 13: Hãy tìm số đảo ngược của số nguyên dương n

def reverse_digits(n: int) -> int:
    return int(str(n)[::-1])

input_n = 1012
print(reverse_digits(input_n))
