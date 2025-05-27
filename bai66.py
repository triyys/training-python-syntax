# Bài 69 (*): Ma trận vuông A với n >= 3. Sắp tam giác dưới giảm dần từ trên xuống dưới và từ trái sang phải.

def triangle_to_array(matrix: list[list[int]]) -> list[int]:
    result = []

    for i in range(len(matrix)):
        for j in range(i + 1):
            result.append(matrix[i][j])

    return result

def reorder(matrix: list[list[int]]) -> None:
    triangle_arr = triangle_to_array(matrix)

    triangle_arr.sort(reverse=True)

    triangle_arr_index = 0

    for i in range(len(matrix)):
        for j in range(i + 1):
            matrix[i][j] = triangle_arr[triangle_arr_index]

            triangle_arr_index += 1

input_matrix = [
    [5, 0, 0, 0],
    [2, 6, 0, 0],
    [9, 4, 1, 0],
    [8, 3, 7, 10],
]
reorder(input_matrix)
print(input_matrix)
