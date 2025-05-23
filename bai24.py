# Bài 24: Viết chương trình nhập vào 1 ngày (ngày, tháng, năm). Tìm ngày kế ngày vừa nhập
from typing import Tuple

MONTH_TYPE = {
    'FULL': [1, 3, 5, 7, 8, 10, 12],
    'PARTIAL': [4, 6, 9, 11],
    'FEBRUARY': [2],
}

def next_date(day: int, month: int, year: int) -> Tuple[int, int, int]:
    if month in MONTH_TYPE['FULL']:
        if day + 1 > 31:
            return (1, 1, year + 1) if month == 12 else (1, month + 1, year)
        else:
            return day + 1, month, year

    if month in MONTH_TYPE['PARTIAL']:
        if day + 1 > 30:
            return 1, month + 1, year
        else:
            return day + 1, month, year

    if month in MONTH_TYPE['FEBRUARY']:
        if day + 1 > 28:
            return 1, month + 1, year
        else:
            return day + 1, month, year

    return day, month, year

input_day = 2
input_month = 1
input_year = 2021
print(next_date(input_day, input_month, input_year))

# Extra test case
result = (23, 5, 2025)
for i in range(100):
    result = next_date(result[0], result[1], result[2])
    print(result)
