T = int(input())
for t in range(1, T+1):
    n = int(input())
    money = list(map(int, input().split()))
    mean = sum(money) / n
    print(f'#{t} {len([x for x in money if x<=mean])}')