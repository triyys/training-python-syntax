# Bài 57: Kiểm tra các giá trị trong ma trận có giảm dần theo dòng và cột hay không.

def is_desc(arr: list[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False

    return True

def is_desc_row(matrix: list[list[int]]) -> bool:
    for row in matrix:
        if not is_desc(row):
            return False

    return True

def is_desc_col(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix[0])):
        col = [row[i] for row in matrix]

        if not is_desc(col):
            return False

    return True

def is_desc_row_and_col(matrix: list[list[int]]) -> bool:
    return is_desc_row(matrix) and is_desc_col(matrix)
