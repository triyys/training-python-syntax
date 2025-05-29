# Bài 61: Hoán vị 2 cột trên ma trận.

def col_permutation(matrix: list[list[int]], index_a: int, index_b: int) -> None:
    for i in range(len(matrix)):
        matrix[i][index_a], matrix[i][index_b] = matrix[i][index_b], matrix[i][index_a]

input_matrix = [
    [-20, 24, -47, -41],
    [22, 32, 37, 1],
    [23, 29, 26, -31],
    [-14, -38, 38, 27]
]
col_permutation(input_matrix, 1, 2)
print(input_matrix)
