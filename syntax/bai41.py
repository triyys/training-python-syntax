# Bài 41: Cho mảng 1 chiều các số nguyên.
# Hãy viết hàm tìm bội chung nhỏ nhất của tất cả các phần tử trong mảng.

def my_gcd(a: int, b: int) -> int:
    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a

def my_lcm(a, b):
    return a * b // my_gcd(a, b)

def find_lcm_all_elements(arr: list[int]) -> int:
    result = arr[0]

    for element in arr:
        result = my_lcm(result, element)

    return result

input_arr = [12, 60, 42, 48, 100, 6, 5]
print(find_lcm_all_elements(input_arr))
