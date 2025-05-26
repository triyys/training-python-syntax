# Bài 39: Cho mảng 1 chiều các số nguyên.
# Hãy viết hàm tìm giá trị lớn nhất trong mảng có dạng 5^k.
# Nếu mảng không tồn tại giá trị 5^k thì hàm sẽ trả về 0.

def is_power_of_five(n: int) -> bool:
    while n > 1:
        n, mod = divmod(n, 5)

        if mod != 0:
            return False

    return True

def find_power_of_five(arr: list[int]) -> int:
    for element in arr:
        if is_power_of_five(element):
            return element

    return 0

input_arr = [3, 8, 125, 625]
print(find_power_of_five(input_arr))
