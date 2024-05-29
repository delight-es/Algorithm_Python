def solution(n, lost, reserve): #학생 수, 체육복 도난 당한 학생, 체육복 가져온 학생
    answer = n-len(lost) #도난 X
    lend = [] #남에게 빌려준 리스트
    lost, reserve = sorted(lost), sorted(reserve)
    
    #1. 잃어버렸지만 체육복 있음
    i = 0
    while i < len(reserve):
        if reserve[i] in lost:
            p = reserve.pop(i)
            lost.pop(lost.index(p))
            lend.append(p)
            i -= 1
        i += 1
    
    #2. 잃어버렸지만 체육복 없음
    for l in lost:
        num = 0
        if l-1 in reserve and l-1 not in lend: #전 학생이 체육복 가짐 + 아직 안빌려줌
            num = l-1
        elif l+1 in reserve and l+1 not in lend: #후 학생이 체육복 가짐 + 아직 안빌려줌
            num = l+1
        
        if num != 0: #누구에게 빌릴 수 있다면
            lend.append(num) #빌려준 학생에 추가

    return answer + len(lend)