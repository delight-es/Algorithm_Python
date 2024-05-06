from collections import deque

for t in range(1,11):
    N, res = int(input()), 0
    lst = list(map(int, input().split()))+[0,0]
    now = deque([lst[i] for i in range(5)])
    for i in range(5,len(lst)):
        s = sorted(now)
        if now[2] == s[-1]: #가장 큰 값이라면
            res += s[-1] - s[-2]
        now.popleft()
        now.append(lst[i])
    print(f"#{t} {res}")