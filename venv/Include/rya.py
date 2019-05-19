from random import randrange, getrandbits

def gyorshatvanyozas(a, n, m):
    actual = a%m
    mod = 1
    while n != 1:
        if n%2 == 1:
            mod=(mod*actual)%m
        actual = (actual**2)%m
        n//=2
    mod *= actual
    return mod%m

def euklidesz(r1, r2):
    q = r1//r2
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1
    temp = 0
    tempx = 0
    tempy = 0
    while(r2 != 0):
        temp = r2
        q = r1 // r2
        r2 = r1%r2
        r1 = temp
        tempx = x2
        x2 = x2*q + x1

        tempy = y2
        x1 = tempx
        y2 = y2*q + y1
        y1 = tempy
    return r1#, q, x1, y1

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:

        return False
    s = 0
    n = num - 1
    while n & 1 == 0:
        s += 1
        n //= 2
    count = 120
    for i in range(count):
        a = 2
        x = gyorshatvanyozas(a, n, num)
        a += 1
        if x != 1 and x != num-1:
            j = 1
            while j < s and x != num-1:
                x = gyorshatvanyozas(x, 2, num)
                if x== 1:
                    return False
                j += 1
            if x != num-1:
                return False
    return True

def generate_prime_candidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    if(is_prime(p)):
        return p
    return generate_prime_candidate(length)

print(gyorshatvanyozas(23, 209, 211))
print(euklidesz(141, 17))
message = 9
print(gyorshatvanyozas(9, 5, 39))
print(gyorshatvanyozas(7, 49*(2**2), 197))
print(is_prime(generate_prime_candidate(1024)))
print(generate_prime_candidate(1024))