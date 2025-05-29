# Bài 22: Nhập vào tháng của 1 năm. Cho biết tháng thuộc quý mấy trong năm

def get_quarter_of_month(month: int) -> int:
    return month // 4 + 1

input_month = 1
print(get_quarter_of_month(input_month))
