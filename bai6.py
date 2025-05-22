# Bài 6: Cho n là số nguyên dương.
# Hãy tìm giá trị nguyên dương k lớn nhất sao cho S(k) < n.
# Trong đó chuỗi k được định nghĩa như sau: S(k) = 1 + 2 + 3 + … + k

def max_k(n: int) -> int:
    k = 1
    current_sum = 1
    while n > current_sum + k + 1:
        k += 1
        current_sum += k
    return k

input_n = 55 # should return 9 because S(10) = 55, not < 55
print(max_k(input_n))
