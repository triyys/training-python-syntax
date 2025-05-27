# Bài 47: Xóa tất cả các phần tử trùng với x.

def remove_duplicate(arr: list[int], x: int) -> None:
    i = 0

    while i < len(arr):
        if arr[i] == x:
            del arr[i]
        else:
            i += 1

input_arr = [-5, 2, 11, 4, 56, 2, -68]
remove_duplicate(input_arr, -5)
print(input_arr)
