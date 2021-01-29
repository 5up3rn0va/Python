def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

a = 512
b = 26

print(gcd(a, b))