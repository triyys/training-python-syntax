# Bài 13: Hãy tìm số đảo ngược của số nguyên dương n

# Không được phép ép kiểu thành str rồi đảo ngược
def reverse_digits(n: int) -> int:
    return int(str(n)[::-1])

input_n = 1012
print(reverse_digits(input_n))
