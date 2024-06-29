from collections import deque
""" 
네트워크
 * n: 컴퓨터 수, computers: 연결 정보 배열
 * a[i][j]가 1이면? i-j 연결
 * (분석) DFS나 BFS로 탐색 --> 연결된 수 구하기
"""

N = 0
a = []
v = []

def solution(n, computers):
    global N, a, v
    answer = 0
    N = n
    a = computers
    v = [False] * N
    for network in range(N):
        if not v[network]:
            #dfs(network)
            bfs(network)
            answer += 1
            print(answer)
    return answer

def dfs(node):
    v[node] = True  # 네트워크 방문 처리
    # 새 네트워크 탐색
    for i in range(N):
        # 방문 X + node와 연결된 네트워크면
        if not v[i] and a[node][i] == 1:
            dfs(i)  # 재귀
            
def bfs(node):
    q = deque()
    v[node] = True  # 네트워크 방문 처리
    q.append(node)  # 큐에 추가
    while q:
        new_node = q.popleft()  # 꺼내서
        # 새 네트워크 탐색
        for i in range(N):
            # 방문 X + node와 연결된 네트워크면
            if not v[i] and a[new_node][i] == 1:
                v[i] = True  #방문 처리
                q.append(i)  # 큐에 추가