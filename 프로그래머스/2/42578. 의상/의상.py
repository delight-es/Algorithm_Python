from collections import Counter

def solution(clothes):
    answer = 1
    c = [x[1] for x in clothes]
    d = Counter(c) # 각 종류 별 해시 만들기
    for v in d.values():
        answer *= (v+1) # 각 종류 +1 (안입는경우) -> 모든 종류 곱
    return answer-1 # 모든 종류 -1 (전체안입는경우)