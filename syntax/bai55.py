# Bài 55 (*): Đếm số lượng giá trị “Hoàng Hậu” trên ma trận.
# Một phần tử được gọi là Hoàng Hậu khi nó lớn nhất trên dòng,
# trên cột và trên 2 đường chéo đi qua nó.

# STT      0    1    2    3    4    5    6    7    8    9    10   11
# Dòng 0 [-20,  24, -47, -41,  24,  -8,  46, -36, -46,  32, -31,  11]
# Dòng 1 [ 22,  32,  37,   1, -36, -43, -20,  -7,  -3, -11,  36,  24]
# Dòng 2 [ 23,  29,  26, -31, -22, -37,  -2,  45,  31, -46, -48,  11]
# Dòng 3 [-14, -38,  38,  27, -37,  -4, -43, -42, -13,  38,  34,  -6]
# Dòng 4 [-43,  -8,  19, -21,  44,  12, -16,  47,  39, -21,  15, -39]
# Dòng 5 [-44,  35, -24,  32,  35,  39, -18,  33,  38,  35, -15,  -2]
# Dòng 6 [-29, -22,  18,  14, -30, -27, -49, -14, -41, -30,  38, -47]
# Dòng 7 [ 46,  23,  -1,   1,  11, -50,  14,  -1, -42,  14, -31, -14]
# Dòng 8 [-15,  -8,  18,  24,  25,   1,  12,  40,  30,  38, -11,  37]

def is_valid_index(matrix: list[list[int]], i: int, j: int) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

def is_max_in_diagonal(matrix: list[list[int]], index_i: int, index_j: int) -> bool:
    diagonal1 = []
    diagonal2 = []

    distance = 1
    while is_valid_index(matrix, index_i - distance, index_j - distance):
        diagonal1.append(matrix[index_i - distance][index_j - distance])
        distance += 1

    distance = 1
    while is_valid_index(matrix, index_i + distance, index_j + distance):
        diagonal1.append(matrix[index_i + distance][index_j + distance])
        distance += 1

    distance = 1
    while is_valid_index(matrix, index_i + distance, index_j - distance):
        diagonal2.append(matrix[index_i + distance][index_j - distance])
        distance += 1

    distance = 1
    while is_valid_index(matrix, index_i - distance, index_j + distance):
        diagonal2.append(matrix[index_i - distance][index_j + distance])
        distance += 1

    return matrix[index_i][index_j] > max(diagonal1) and matrix[index_i][index_j] > max(diagonal2)

def is_max_in_row(matrix: list[list[int]], index_i: int, index_j: int) -> bool:
    return max(matrix[index_i]) == matrix[index_i][index_j]

def is_max_in_col(matrix: list[list[int]], index_i: int, index_j: int) -> bool:
    col = [row[index_j] for row in matrix]

    return max(col) == matrix[index_i][index_j]

def queen_count(matrix: list[list[int]]) -> int:
    result = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if is_max_in_row(matrix, i, j) and is_max_in_col(matrix, i, j) and is_max_in_diagonal(matrix, i, j):
                result += 1

    return result

input_matrix = [
    [-20, 24, -47, -41, 24, -8, 46, -36, -46, 32, -31, 11],
    [22, 32, 37, 1, -36, -43, -20, -7, -3, -11, 36, 24],
    [23, 29, 26, -31, -22, -37, -2, 45, 31, -46, -48, 11],
    [-14, -38, 38, 27, -37, -4, -43, -42, -13, 38, 34, -6],
    [-43, -8, 19, -21, 44, 1200, -16, 47, 39, -21, 15, -39],
    [-44, 35, -24, 32, 35, 39, -18, 33, 38, 35, -15, -2],
    [-29, -22, 18, 14, -30, -27, -49, -14, -41, -30, 38, -47],
    [46, 23, -1, 1, 11, -50, 14, -1, -42, 14, -31, -14],
    [-15, -8, 18, 24, 25, 1, 12, 40, 30, 38, -11, 37],
]
print(queen_count(input_matrix))
