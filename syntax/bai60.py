# Bài 60: Hoán vị 2 dòng trên ma trận.

def row_permutation(matrix: list[list[int]], index_a: int, index_b: int) -> None:
    for i in range(len(matrix[0])):
        matrix[index_a][i], matrix[index_b][i] = matrix[index_b][i], matrix[index_a][i]

input_matrix = [
    [-20, 24, -47, -41],
    [22, 32, 37, 1],
    [23, 29, 26, -31],
    [-14, -38, 38, 27]
]
row_permutation(input_matrix, 1, 2)
print(input_matrix)
