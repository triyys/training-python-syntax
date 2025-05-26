# Bài 30: Viết hàm đếm số lượng số nguyên tố nhỏ hơn 100 trong mảng

def is_prime_number(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_number_count(arr: list[int]) -> int:
    return len([element for element in arr if element < 100 and is_prime_number(element)])

input_arr = [3, 5, 29, 3000, 137, 139]
print(prime_number_count(input_arr))
