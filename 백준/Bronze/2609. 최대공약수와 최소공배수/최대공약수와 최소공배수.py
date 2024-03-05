A, B = map(int, input().split())
max_div, min_mul = 0,0

def gcd(a,b):
    if (a < b):
        temp = b
        b, a = a, temp
    while (b > 0):
        a, b = b, a%b
    return a

def lcm(a,b, max_div):
    return a*b // max_div

max_div = gcd(A,B)
min_mul = lcm(A,B,max_div)

print(max_div)
print(min_mul)