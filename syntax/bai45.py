# Bài 45: Thêm x vào trong mảng tăng nhưng vẫn giữ nguyên tính tăng của mảng.

def insert(arr: list[int], x: int) -> None:
    for index_arr, value_arr in enumerate(arr):
        if x < value_arr:
            arr.insert(index_arr, x)
            return

    arr.append(x)

input_arr = [1, 3, 6, 7, 7, 7, 8, 12]
input_x = 7
insert(input_arr, input_x)
print(input_arr)
