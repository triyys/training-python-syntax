# Bài 25: Viết chương trình nhập vào 1 ngày (ngày, tháng, năm). Tìm ngày trước ngày vừa nhập
from typing import Tuple
import calendar

# Sao lại chơi thư viện rồi
def previous_date(day: int, month: int, year: int) -> Tuple[int, int, int]:
    if day - 1 == 0:
        if month - 1 == 0:
            return 31, 12, year - 1
        else:
            return calendar.monthrange(year, month - 1)[1], month - 1, year

    return day - 1, month, year

input_day = 2
input_month = 1
input_year = 2021
print(previous_date(input_day, input_month, input_year))

# Extra test case
result = (23, 5, 2025)
for i in range(100):
    result = previous_date(result[0], result[1], result[2])
    print(result)
