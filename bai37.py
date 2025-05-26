# Bài 37: Cho mảng 1 chiều các số nguyên.
# Hãy tìm giá trị đầu tiên có chữ số đầu tiên là chữ số lẻ.
# Nếu mảng không có giá trị lẻ thì hàm sẽ trả về 0.
# => Tức là kiểm tra mảng chẵn hết

def is_even_array(arr: list[int]) -> bool:
    return all([value % 2 == 0 for value in arr])

input_arr = [2, 4, -6, 88, 24]
print(is_even_array(input_arr))
