# Bài 21: Cho 2 số nguyên dương a và b. Hãy tìm ước chung lớn nhất và tìm bội chung nhỏ nhất của 2 số này

def my_gcd(a, b):
    if b == 0:
        return a
    return my_gcd(b, a % b)

def my_lcm(a, b):
    return a * b // my_gcd(a, b)

input_a = 12
input_b = 8
print(my_gcd(input_a, input_b))
print(my_lcm(input_a, input_b))
