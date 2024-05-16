import sys
sys.setrecursionlimit(10**6)

n,m,r = map(int, sys.stdin.readline().split()) #정점수,간선수,시작점
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
c = 1
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for a,b in arr:
    graph[a].extend([b])
    graph[b].extend([a])
graph = [sorted(a) for a in graph]

def dfs(graph, v, visited): #스택,재귀
     global c
     visited[v] = c
     c += 1
     for i in graph[v]:
         if visited[i] == 0:
             dfs(graph, i, visited)

dfs(graph, r, visited)

for i in range(1,len(visited)):
    print(visited[i])