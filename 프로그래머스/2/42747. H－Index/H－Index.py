"""
 * H-index
 * citations: 논문 인용횟수 배열
 * 발표 논문 n개 중 h번 이상 인용된 게 h편 이상,
나머지 논문이 h번 이하 인용 -> h 최댓값
(분석) 내림차순 정렬 -> 하나씩 줄여보며 -> 값이 h 이상인 원소 개수=h이상인지 확인 / (나머지)전체-h이상 원소개수=h이하인지 확인
"""

def solution(citations):
    c = sorted(citations, reverse=True)
    print(c)
    # 값이 h와 같거나 큰 원소 개수 >= h and (전체 개수 - 앞 개수) <= h:
    h = c[0]
    while h >= 0:
        num = len([x for x in c if x >= h])
        if num >= h:
            return h
        h -= 1