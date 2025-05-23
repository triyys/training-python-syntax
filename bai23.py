# Bài 23: Viết chương trình nhập 3 cạnh của 1 tam giác, cho biết đó là tam giác gì

def calculate_triangle_type(a: float, b: float, c: float) -> str:
    if a + b <= c or b + c <= a or c + a <= b:
        return 'Invalid triangle'

    if a == b and a == c:
        return 'Equilateral triangle'

    if a == b or b == c or a == c:
        return 'Isosceles triangle'

    sorted_edges = [a, b, c]
    sorted_edges.sort()
    if sorted_edges[0] ** 2 + sorted_edges[1] ** 2 == sorted_edges[2] ** 2:
        return 'Right triangle'

    return 'Triangle'

input_a = 3
input_b = 5
input_c = 4
print(calculate_triangle_type(input_a, input_b, input_c))
