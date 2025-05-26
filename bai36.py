# Bài 36: Cho mảng 1 chiều các số nguyên. Hãy tìm giá trị đầu tiên thỏa mãn tính chất số gánh

def is_palindrome(n: int) -> bool:
    reversed_n = 0
    # Clone n to iterate without affecting original n
    mutable_n = n

    while mutable_n > 0:
        mutable_n, remainder = divmod(mutable_n, 10)
        reversed_n = reversed_n * 10 + remainder

    return n == reversed_n

def find_palindrome(arr: list[int]) -> int:
    for value in arr:
        if is_palindrome(value):
            return value

    return -1

input_arr = [123, 656]
print(find_palindrome(input_arr))
