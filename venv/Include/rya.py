from random import randrange, getrandbits, randint
import sys
sys.setrecursionlimit(10**6)


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
    if r2 == 0: return r1
    return euklidesz(r2, r1%r2)

def euklideszEx(r1, r2):
    q = r1//r2
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1
    temp = 0
    tempx = 0
    tempy = 0
    counter = 0
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
        counter += 1
    X = ((-1)**counter) * x1
    Y = ((-1)**(counter+1)) * y1
    return r1, X, Y

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

def found_e(fn, n):
    e = 3
    while True:
        if euklidesz(fn, e) == 1: break
        else: e = e + 2
    return e

def kinai(p, q, d, message):
    M = p*q
    c1=gyorshatvanyozas(message,d%(p-1),p)
    c2=gyorshatvanyozas(message,d%(q-1),q)
    b,x0,y0=euklideszEx(p,q)
    y1,y2=x0,y0
    print((y1 * p) % q)
    print((y2 * q) % p)
    return (c1*y1*p+c2*y2*q)%M

p = generate_prime_candidate(1024)
print("A generált p érték:\n", p)
q = generate_prime_candidate(1024)
print("A generált q érték:\n", q)
message = 9
n = p*q
fn = (p-1)*(q-1)
print("Az n értéke:\n", n)
print("A fn értéke:\n", fn)
e = found_e(fn, n)
print("Private\n", e, n)
d = euklideszEx(fn,e)[2]
print("A d értéke:", d)
titkos = gyorshatvanyozas(message, e, n)
print("Az üzenet:", message)
print("A kódolt üzenet:", titkos)
visszafejt=kinai(p,q,d,titkos)
print("Az üzenet visszafejtve:", visszafejt)

