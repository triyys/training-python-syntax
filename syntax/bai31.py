# Bài 31: Viết hàm tính tổng các giá trị âm trong mảng 1 chiều các số thực

def sum_negative(arr: list[float]) -> float:
    result = 0

    for element in arr:
        if element < 0:
            result += element

    return result

input_arr = [3.2, 11.5, -54.2, 12.7]
print(sum_negative(input_arr))
