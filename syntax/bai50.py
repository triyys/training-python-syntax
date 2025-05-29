# Bài 50 (*): Cho mảng a, số nguyên M. Tìm 1 mảng con sao cho tổng các phần tử bằng M.

def sum_equal_sub_string(arr: list[int], m: int) -> list[int]:
    for head in range(len(arr) - 1):
        for tail in range(head + 1, len(arr)):
            if sum(arr[head : tail + 1]) == m:
                return arr[head : tail + 1]

    return []

input_arr = [1, 2, 1, 3]
input_m = 6
print(sum_equal_sub_string(input_arr, input_m))
