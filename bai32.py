# Bài 32: Viết hàm sắp xếp mảng 1 chiều các số thực tăng dần

def sort_real(arr: list[float]) -> None:
    arr.sort()

input_arr = [5, 24, -53, 8, 6, 100, -31, 19]
sort_real(input_arr)
print(input_arr)
