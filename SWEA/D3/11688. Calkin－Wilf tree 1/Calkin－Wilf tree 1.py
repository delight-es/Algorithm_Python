T = int(input())

for t in range(1,T+1):
    st = input()
    a,b = 1,1
    for s in st:
        if s == 'L':
            a,b = a, a+b
        else:
            a,b = a+b, b
    print(f"#{t} {a} {b}")