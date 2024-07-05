"""
 ** 정렬(가장큰수)
 * numbers: 숫자배열
 * answer: 정답배열
 * (분석) 문자배열로 변환 -> 원소 차근차근 앞/뒤에 붙여 비교
 (!) 내림차순 정렬 X 
 반례: {3, 30, 34, 5, 9}
 >> (정렬)9534303 < (답)"9534330"
 (!) 0만 있으면 0출력: (ex) {0,0}
 >> (기존) 00 -> (예외처리) 0(O)
 
"""    
# 커스텀 정렬 라이브러리
from functools import cmp_to_key

def compare(a, b):
    if a+b > b+a: # 앞에 붙인게 크면
        return -1 # 앞의 친구를 앞으로
    elif a+b < b+a: # 뒤에 붙인게 크면
        return 1 #앞의 친구를 뒤로
    else: # 같으면
        return 0

def solution(numbers):
    s = [str(num) for num in numbers]
    s.sort(key=cmp_to_key(compare)) #key로 전달
    if s[0] == '0':
        return '0'
    return ''.join(s)