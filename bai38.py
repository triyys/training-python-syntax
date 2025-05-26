# Bài 38: Cho mảng 1 chiều các số nguyên.
# Hãy viết hàm tìm giá trị đầu tiên trong mảng có dạng 2^k.
# Nếu mảng không có giá trị dạng 2^k thì hàm sẽ trả về 0.

def is_power_of_two(n: int) -> bool:
    while n > 1:
        if n % 2 == 1:
            return False
        else:
            n = n // 2

    return True

def find_power_of_two(arr: list[int]) -> int:
    for element in arr:
        if is_power_of_two(element):
            return element

    return 0

input_arr = [3, 8]
print(find_power_of_two(input_arr))
