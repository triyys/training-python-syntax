# Bài 54 (*): Đếm số lượng giá trị phân biệt có trong ma trận các số thực.

def to_array(matrix: list[list[float]]) -> list[float]:
    result = []

    for row in matrix:
        for cell in row:
            result.append(cell)

    return result

def unique_count(matrix: list[list[float]]) -> int:
    elements = to_array(matrix)

    result = len(elements)
    duplicate_element_count = 0
    hashtable = {}

    for element in elements:
        if element in hashtable:
            result -= 1
            duplicate_element_count += 1
        else:
            hashtable.update({ element: True })

    return result - duplicate_element_count

input_matrix = [
    [ 1, 75, 53,  1, 14,  7],
    [18, 98, 70, 71, 81,  2],
    [62, 88, 26, 93, 95, 99],
]
print(unique_count(input_matrix))
