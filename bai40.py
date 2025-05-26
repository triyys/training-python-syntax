# Bài 40: Cho mảng 1 chiều các số nguyên.
# Hãy viết hàm tìm ước chung lớn nhất của tất cả các phần tử trong mảng.

def my_gcd(a: int, b: int) -> int:
    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a

def find_gcd_all_elements(arr: list[int]) -> int:
    result = arr[0]

    for element in arr:
        result = my_gcd(result, element)

    return result

input_arr = [12, 60, 42, 48]
print(find_gcd_all_elements(input_arr))
