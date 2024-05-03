from collections import deque
def solution(s):
    q = deque([x for x in s])
    if s.count('(') != s.count(')'): # 개수 다르면 X
        return False
    else: # 개수 같으면
        open, close  = 0, 0
        while len(q) >= 1:
            p = q.popleft() # 하나씩 지우면서
            if p == '(': #(로 시작
                open += 1
            else: #)로 시작
                close += 1
                if close > open: #만약 닫는 게 더 크면
                    return False
        return True