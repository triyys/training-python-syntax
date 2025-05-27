# Bài 48: Hãy đưa chẵn về đầu, lẻ về cuối, phần tử 0 nằm giữa.

def format_even_odd(arr: list[int]) -> list[int]:
    even = []
    odd = []
    zero = []
    for element in arr:
        if element == 0:
            zero.append(element)
        elif element % 2 == 0:
            even.append(element)
        elif element % 2 == 1:
            odd.append(element)

    return even + zero + odd

input_arr = [6, 53, 10, 0, 8, 101, 31, 19, 42424]
print(format_even_odd(input_arr))
