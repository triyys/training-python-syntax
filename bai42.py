# Bài 42: Cho mảng 1 chiều các số nguyên.
# Hãy viết hàm tìm chữ số xuất hiện nhiều nhất trong mảng.

def most_frequency(arr: list[int]) -> int:
    obj = {}
    result = arr[0]

    for element in arr:
        if element in obj:
            obj[element] += 1
        else:
            obj.update({ element: 1 })

        if obj[element] > obj[result]:
            result = element

    return result

input_arr = [1, 1, 1, 7, 7, 2, 2, 1, 3, 1, 2, 8, 2, 2, 2]
print(most_frequency(input_arr))
