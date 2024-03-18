import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
S = [[0 for _ in range(N+1)] for _ in range(N+1)]

arr.append([0 for _ in range(N+1)])
for i in range(N):
    arr.append([0] + list(map(int, input().split())))

for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + arr[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(S[x2][y2]-S[x1-1][y2]-S[x2][y1-1]+S[x1-1][y1-1])