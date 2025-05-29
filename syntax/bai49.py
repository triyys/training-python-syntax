# Bài 49: Đếm mảng con tăng có độ dài lớn hơn 1.

def is_asc(arr: list[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True

def asc_sub_string_count(arr: list[int]) -> int:
    result = 0

    for head in range(len(arr) - 1):
        for tail in range(head + 1, len(arr)):
            if is_asc(arr[head : tail + 1]):
                result += 1

    return result

input_arr = [1, 2, 1, 3]
print(asc_sub_string_count(input_arr))
