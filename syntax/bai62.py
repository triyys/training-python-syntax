# Bài 62: Xóa 1 dòng trong ma trận.

def remove_row(matrix: list[list[int]], index: int) -> None:
    matrix.pop(index)

input_matrix = [
    [-20, 24, -47, -41],
    [22, 32, 37, 1],
    [23, 29, 26, -31],
    [-14, -38, 38, 27]
]
remove_row(input_matrix, 1)
print(input_matrix)
