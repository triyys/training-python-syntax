# Bài 51: Tính tích các giá trị dương trên 1 cột trong ma trận các số nguyên.

def product_positive_column(matrix: list[list[int]], column_index: int) -> int:
    column_array = [matrix[i][column_index] for i in range(len(matrix))]

    result = 1

    for element in column_array:
        if element > 0:
            result *= element

    return result

input_matrix = [
    [1, 2, 3],
    [2, 5, 6],
    [7, 5, 8],
    [8, -2, 12]
]
input_column_index = 1
print(product_positive_column(input_matrix, input_column_index))
