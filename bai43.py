# Bài 43 (*): Cho mảng số thực có nhiều hơn 2 giá trị
# và các giá trị trong mảng khác nhau từng đôi một.
# Hãy viết hàm tìm 2 giá trị gần nhau nhất trong mảng
# (Lưu ý: Mảng có các giá trị khác nhau từng đôi một còn có tên là mảng phân biệt).

def find_closet_pair(arr: list[float]) -> tuple[float, float]:
    mutable_arr = arr.copy()
    mutable_arr.sort()

    result = mutable_arr[0], mutable_arr[1]

    for i in range(1, len(mutable_arr)):
        current_distance = mutable_arr[i] - mutable_arr[i - 1]

        if current_distance < result[1] - result[0]:
            result[0], result[1] = mutable_arr[i - 1], mutable_arr[i]

    return result

input_arr = [3, 9, 4, 33, 2.5]
print(find_closet_pair(input_arr))
