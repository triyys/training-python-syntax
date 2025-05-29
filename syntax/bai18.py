# Bài 18: Hãy kiểm tra số nguyên dương n có phải là số đối xứng hay không

def is_palindrome(n: int) -> bool:
    reversed_n = 0
    mutable_n = n # Tạo ra cái này để làm gì

    while mutable_n > 0:
        mutable_n, remainder = divmod(mutable_n, 10)
        reversed_n = reversed_n * 10 + remainder

    # Con điên.
    # return n == reversed_n là đủ
    return True if n == reversed_n else False

input_n = 1235321
print(is_palindrome(input_n))
