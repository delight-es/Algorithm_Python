T = int(input())

for i in range(T):
    N = int(input())
    a,b,c,d,e=0,0,0,0,0
    while N>1:
        if N%2 == 0:
            N, a = N//2, a+1
        elif N%3 == 0:
            N, b = N//3, b+1
        elif N%5 == 0:
            N, c = N//5, c+1
        elif N%7 == 0:
            N, d = N//7, d+1
        elif N%11 == 0:
            N, e = N//11, e+1
    print('#'+str(i+1),a,b,c,d,e)

    
