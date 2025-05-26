# Bài 29: Viết hàm kiểm tra trong mảng các số nguyên
# có tồn tại giá trị x chẵn nhỏ hơn 2004 hay không

def is_valid_array(arr: list[int]) -> bool:
    for element in arr:
        if element % 2 == 0 and element < 2004:
            return True

    return False

input_arr = [2025, 2112, 2005]
print(is_valid_array(input_arr))
