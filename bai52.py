# Bài 52: Tính tổng các giá trị nằm trên biên của ma trận.

def sum_column_except_bounds(matrix: list[list[int]], column_index: int) -> int:
    return sum([row[column_index] for row in matrix[1 : len(matrix) - 1]])

def sum_bound_value(matrix: list[list[int]]) -> int:
    if len(matrix) == 1:
        return sum(matrix[0])

    if len(matrix) == 2:
        return sum(matrix[0]) + sum(matrix[len(matrix) - 1])

    if len(matrix[0]) == 1:
        return sum([row[0] for row in matrix])

    first_row_sum = sum(matrix[0])
    last_row_sum = sum(matrix[len(matrix) - 1])
    first_column_sum = sum_column_except_bounds(matrix, 0)
    last_column_sum = sum_column_except_bounds(matrix, len(matrix[0]) - 1)

    return first_row_sum + last_row_sum + first_column_sum + last_column_sum

input_matrix = [
    [1, 2, 3],
    [2, 5, 6],
    [7, 5, 8],
    [8, -2, 12]
]
print(sum_bound_value(input_matrix))
