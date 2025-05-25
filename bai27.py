# Bài 27: Viết hàm tìm giá trị lớn nhất trong mảng 1 chiều các số thực
from typing import List

# Điều gì xảy ra khi so sánh 2 số thực?
def max_real(l: List[float]) -> float:
    result = l[0]

    for i in l:
        if i > result:
            result = i

    return result

input_l = [5, 24.05, -53.11, 24.06, 24.07]
print(max_real(input_l))
