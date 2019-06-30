def fak(n):
    if n != 0:
        result = n * fak(n-1)
        return result
    else:
        return 1
def sinus(x, accuracy):
    result = 0
    n = 0
    while n < accuracy:
        result = result + (-1)**n * x**(2*n+1) / fak(2*n+1)
        n += 1
    return result
def cosinus(x, accuracy):
    result = 0
    n = 0
    while n < accuracy:
        result = result + (-1)**n * x**(2*n) / fak(2*n)
        n += 1
    return result

print sinus(0, 5)
print cosinus(0, 5)
