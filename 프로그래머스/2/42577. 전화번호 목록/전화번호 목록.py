def solution(phone_book):
    d = {}
    for p in phone_book: #딕셔너리 d 정의
        d[p] = 1
        
    for p in phone_book: #각 번호마다
        num = ""
        for n in range(len(p)-1): #맨 끝번호 빼고
            num += p[n] #번호 한글자씩 추가
            if (num in d): #해시에 있으면
                return False
    return True