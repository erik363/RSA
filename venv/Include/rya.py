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
    for a in range(2, 120):
        if (euklidesz(a, num) == 1):
            s = 0
            numDS = num-1
            while(numDS%2 == 0):
                numDS = numDS/2
                s = s+1
            d = numDS
            print("ennyi a d",d)
            for r in range(s):
                if(gyorshatvanyozas(a, d, num) == num-1):
                    print("teljesült")
                    return True
                else:
                    d = d * (2 ** r)
        else:
            return False



print(gyorshatvanyozas(23, 209, 211))
print(euklidesz(141, 17))
message = 9
print(gyorshatvanyozas(9, 5, 39))
print(gyorshatvanyozas(7, 49*(2**2), 197))
print(is_prime(21))