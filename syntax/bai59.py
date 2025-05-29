# Bài 59 (*): Liệt kê các cột có nhiều chữ số nhất trong ma trận các số nguyên.

def digit_count(n: int) -> int:
    result = 0

    while n > 0:
        result += 1
        n = n // 10

    return result

def array_digit_count(arr: list[int]) -> int:
    result = 0

    for element in arr:
        result += digit_count(element)

    return result

# Only return first column for simplicity
def max_digit_col(matrix: list[list[int]]) -> list[int]:
    max_value = 0
    result = []

    for i in range(len(matrix[0])):
        col = [row[i] for row in matrix]

        col_digit_count = array_digit_count(col)

        if col_digit_count > max_value:
            max_value = col_digit_count
            result = col

    return result

input_matrix = [
    [132, 3, 546, 78, 901, 23],
    [544, 7, 89, 12, 4, 546],
    [784, 9404, 12, 4, 56, 7800]
]
print(max_digit_col(input_matrix))
