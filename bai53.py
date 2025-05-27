# Bài 53 (*): Đếm số lượng phần tử cực trị trong ma trận các số thực.
# Một phần tử được gọi là cực trị khi nó lớn hơn các phần tử xung quanh
# hoặc nhỏ hơn các phần tử xung quanh.

def is_valid_index(matrix: list[list[int]], i: int, j: int) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

def get_surrounded_elements(matrix: list[list[int]], center_i: int, center_j: int) -> list[int]:
    result = []

    positions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for position in positions:
        if is_valid_index(matrix, center_i + position[0], center_j + position[1]):
            result.append(matrix[center_i + position[0]][center_j + position[1]])

    return result

def is_max_element(surrounded_elements: list[int], center_element: int):
    return center_element > max(surrounded_elements)

def max_element_count(matrix: list[list[int]]) -> int:
    result = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if is_max_element(get_surrounded_elements(matrix, i, j), matrix[i][j]):
                result += 1

    return result

input_matrix = [
    [-20, 24, -47, -41, 24, -8, 46, -36, -46, 32, -31, 11],
    [22, 32, 37, 1, -36, -43, -20, -7, -3, -11, 36, 24],
    [23, 29, 26, -31, -22, -37, -2, 45, 31, -46, -48, 11],
    [-14, -38, 38, 27, -37, -4, -43, -42, -13, 38, 34, -6],
    [-43, -8, 19, -21, 44, 12, -16, 47, 39, -21, 15, -39],
    [-44, 35, -24, 32, 35, 39, -18, 33, 38, 35, -15, -2],
    [-29, -22, 18, 14, -30, -27, -49, -14, -41, -30, 38, -47],
    [46, 23, -1, 1, 11, -50, 14, -1, -42, 14, -31, -14],
    [-15, -8, 18, 24, 25, 1, 12, 40, 30, 38, -11, 37]
]
print(max_element_count(input_matrix))
