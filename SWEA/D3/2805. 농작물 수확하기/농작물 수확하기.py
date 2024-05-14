T = int(input())

for t in range(1,T+1):
    n, res = int(input()), 0
    arr = [[int(i) for i in input()] for _ in range(n)]

    key = n // 2
    for i in range(n):
        if i <= key:
            res += sum(arr[i][key-i:key+i+1])
        else:
            res += sum(arr[i][i-key:key+(n-i)])

    print(f"#{t} {res}")