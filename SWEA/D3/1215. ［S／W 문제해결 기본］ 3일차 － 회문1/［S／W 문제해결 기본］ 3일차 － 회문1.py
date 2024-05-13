# CBBCBAAB
from collections import deque

for i in range(1, 11):
    n, res = int(input()), 0 #회문 길이, 정답
    arr = [input() for _ in range(8)]

    #가로
    for x in range(8):
        a = deque(arr[x][:n])
        if ''.join(list(a)) == ''.join(list(a))[::-1]:
            res += 1
        for y in range(n,8):
            a.popleft()
            a.append(arr[x][y])
            if ''.join(list(a)) == ''.join(list(a))[::-1]:
                res += 1

    # 세로
    for x in range(8):
        b = deque()
        for j in range(n):
            b.append(arr[j][x])
        if ''.join(list(b)) == ''.join(list(b))[::-1]:
            res += 1
        for y in range(n, 8):
            b.popleft()
            b.append(arr[y][x])
            if ''.join(list(b)) == ''.join(list(b))[::-1]:
                res += 1

    print(f"#{i} {res}")