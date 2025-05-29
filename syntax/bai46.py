# Bài 46: Hãy xóa tất cả số lớn nhất trong mảng các số thực.

def remove_max_numbers(arr: list[float]) -> None:
    max_value = max(input_arr)
    i = 0

    while i < len(arr):
        if arr[i] == max_value:
            del arr[i]
        else:
            i += 1

input_arr = [-5.9, 2.2, 11.32, 4.3, 56.2, 2.1, -68]
remove_max_numbers(input_arr)
print(input_arr)
