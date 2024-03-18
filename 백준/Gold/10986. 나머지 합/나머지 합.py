import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
S, S_div = [0 for _ in range(N)], [0 for _ in range(N)]
C = [0 for _ in range(M)]
res = 0

for i in range(N):
    if i == 0: #처음 합
        S[i] = arr[0]
    else: #이후 합
        S[i] = S[i - 1] + arr[i]

    S_div[i] = S[i] % M # 나머지
    if (S_div[i] == 0):
        res += 1
    C[S_div[i]] += 1 # 카운트 (나머지에 해당하는 인덱스에 +1)

for i in range(M):
    if C[i] >= 2:
        res += C[i] * (C[i]-1) // 2 #C[i]개 중 2개 뽑을 확률 계산

print(res)