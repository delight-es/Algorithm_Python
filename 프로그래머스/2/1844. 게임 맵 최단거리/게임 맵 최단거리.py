from collections import deque

# 게임맵최단거리
# 시작점(1,1) ~ 끝점(n,m)으로 우좌하상(동서남북) 이동
# arr 배열: 0(벽-검정), 1(길-흰색)
# 가장 지나는 최소 칸수 --> 출력! (단, 도착 못하면 -1)
# (분석) 최단거리 => BFS

def bfs(i, j, cnt, arr, v, N, M):
    # 우좌하상
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    q = deque()
    v[i][j] = True  # 방문처리
    q.append((i,j,cnt))  # 큐 넣기
    
    while q:
        i, j, c = q.popleft()  # 꺼내서
        # 처리
        arr[i][j] = c
        for d in range(4):  # 새 좌표 탐색
            ni = i + di[d]
            nj = j + dj[d]
            nc = c + 1
            # 범위 정상 + 방문 X + 길이면
            if (0<=ni<N) and (0<=nj<M) and (not v[ni][nj]) and (arr[ni][nj] == 1):
                v[ni][nj] = True  # 방문처리
                arr[ni][nj] += arr[i][j]  # 이전이동+1
                q.append((ni, nj, nc))  # 큐에 넣기

def solution(maps):
    #1. 입력    
    N = len(maps)
    M = len(maps[0])
    v = [[False] * M for _ in range(N)]
    
    #2. 처리
    bfs(0, 0, 1, maps, v, N, M) # x,y,cnt,배열,방문,배열크기-x,y

    #3. 출력
    answer = -1 if maps[N-1][M-1] <= 1 else maps[N-1][M-1]
    return answer