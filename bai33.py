# Bài 33: Hãy tìm giá trị k trong mảng các số thực xa giá trị x nhất

def largest_distance(arr: list[float], x: float) -> float:
    result = arr[0]

    for value in arr:
        if abs(x - result) < abs(x - value):
            result = value

    return result

input_arr = [100, -44, -29.7, 88.3, -89, 55, 84.34]
input_x = 86
print(largest_distance(input_arr, input_x))
