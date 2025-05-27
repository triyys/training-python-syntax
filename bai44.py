# Bài 44 (*): Cho 2 mảng a, b. Hãy cho biết số lần xuất hiện của mảng a trong mảng b.

def sub_array_count(a: list[int], b: list[int]) -> int:
    result = 0

    for i in range(0, len(b) - len(a) + 1):
        if b[i : i + len(a)] == a:
            result += 1

    return result

input_a = [1, 1]
input_b = [1, 3, 1, 2, 3, 1, 1, 1, 3]
print(sub_array_count(input_a, input_b))
