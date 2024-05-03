from collections import deque #선입선출

def solution(progresses, speeds):
    answer, q = [], deque(progresses)
    while len(q) >= 1:
        job = 0
        # 한 작업씩 작업 일 추가
        for i in range(len(q)):
            q[i] += speeds[i]
        # 모든 작업에 대해
        for _ in range(len(q)):
            if q[0] >= 100: #앞선 작업이 100 넘으면
                q.popleft() #삭제
                speeds.pop(0)
                job += 1 # 개수+1
            else: #못 넘으면
                break
        if job != 0:
            answer.append(job)
    return answer