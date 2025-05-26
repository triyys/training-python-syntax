# Bài 35: Cho mảng 1 chiều các số thực.
# Hãy viết hàm tìm một vị trí k trong mảng thỏa 2 điều kiện:
# có 2 giá trị lân cận và giá trị tại đó bằng tích 2 giá trị lân cận.
# Nếu mảng không tồn tại giá trị như vậy thì trả về giá trị -1

def find_valid_nearby(arr: list[float]) -> int:
    if len(arr) < 3:
        return -1

    for i in range(1, len(arr) - 1):
        if arr[i] == arr[i - 1] * arr[i + 1]:
            return i

    return -1

input_arr = [100, -44, -29.7, 88.3, -89, 11, 55, 5, 84.34]
print(find_valid_nearby(input_arr))
