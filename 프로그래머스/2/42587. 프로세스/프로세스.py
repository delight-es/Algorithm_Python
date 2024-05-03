from collections import deque #선입선출

def solution(priorities, location):
    answer = []
    lst = deque([(i,p) for i,p in enumerate(priorities)]) #인덱스-우선순위
    while (len(lst) >= 1):
        m, p = max(priorities), lst.popleft() # 최대 값 구하기
        if p[1] == m: #우선순위 = 최대
            answer.append(p[0]) #answer에 인덱스 추가
            priorities.pop(priorities.index(m))
        else:
            lst.append(p)
    return answer.index(location)+1