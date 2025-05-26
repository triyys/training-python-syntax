# Bài 28: Viết hàm tìm 1 vị trí mà giá trị tại vị trí đó
# là giá trị nhỏ nhất trong mảng 1 chiều các số nguyên

def find_min_index(arr: list[int]) -> int:
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i

    return min_index

input_arr = [5, 24.05, -53.11, 24.06, 24.07]
print(find_min_index(input_arr))
