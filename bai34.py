# Bài 34: Cho mảng 1 chiều các số thực, hãy tìm giá trị x sao cho đoạn [-x, x] chứa tất cả các giá trị trong mảng

def find_range(arr: list[float]) -> float:
    result = 0

    for value in arr:
        if abs(value) > result:
            result = abs(value)

    return result

input_arr = [100, -44, -29.7, 88.3, -89, 55, 84.34]
print(find_range(input_arr))
