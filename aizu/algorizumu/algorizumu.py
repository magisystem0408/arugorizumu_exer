"""
最大公約数の求め方
"""

def calc_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return calc_gcd(b, a % b)


input = input()

a, b = [int(elem) for elem in input.split()]

print(calc_gcd(a, b))
