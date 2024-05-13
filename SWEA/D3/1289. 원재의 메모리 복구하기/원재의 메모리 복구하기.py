T = int(input())
for i in range(1, T+1):
    res, s = 0, input()
    origin = '0'*len(s)

    x = 0
    while origin != s:
        if origin[x] != s[x]:
            origin = origin[:x] + s[x]*(len(s)-x)
            res += 1
        x += 1

    print(f"#{i} {res}")