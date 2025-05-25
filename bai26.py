# Bài 26: Viết chương trình in ra tam giác cân có độ cao h
# a. Tam giác cân đặc
# b. Tam giác cân rỗng
# c. Tam giác vuông cân đặc
# d. Tam giác vuông cân rỗng

#     *     0   8   1
#    ***    1   6   3
#   *****   2   4   5
#  *******  3   2   7
# ********* 4   0   9
# 012345678

def generate_equilateral_triangle(h: int) -> str:
    return '\n'.join([' ' * (h - i + 1) + '*' * (2 * i + 1) + ' ' * (h - i + 1) for i in range(h)])

print(generate_equilateral_triangle(5))
