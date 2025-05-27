# Bài 65 (*): Ma trận vuông A(n x n) với n >= 3. Sắp tam giác trên tăng dần từ trên xuống dưới và từ trái sang phải.

def triangle_to_array(matrix: list[list[int]]) -> list[int]:
    result = []

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            result.append(matrix[i][j])

    return result

def reorder(matrix: list[list[int]]) -> None:
    triangle_arr = triangle_to_array(matrix)

    triangle_arr.sort()

    triangle_arr_index = 0

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j] = triangle_arr[triangle_arr_index]

            triangle_arr_index += 1

input_matrix = [
    [5, 8, 3, 7],
    [0, 6, 2, 9],
    [0, 0, 1, 4],
    [0, 0, 0, 10],
]
reorder(input_matrix)
print(input_matrix)
