# def solution(clothes):
#     answer = len(clothes)
#     c = [x[1] for x in clothes]
#     n = len(set(c))
#     print(n, c)
#     # while n >= 1:
#     #     set
#     return answer


# # 3개를 뽑는다? 2,1,1 -> 2개 = 2
# # 3개를 뽑는다? 2,1,2 -> ab,c,de 4개 = 4
# # 3개를 뽑는다? 3,1,2 -> abc, d, ef 6개 = 6


# # 2개를 뽑는다? 2,1,1 -> ab,c,d -> 4개 
# # 2개를 뽑는다? 2,1,2 -> ab,c,de -> 8개
# # 2개를 뽑는다? 3,1,2 -> abc, d, ef -> 9개

# # 1개를 뽑는다? 2,1,1 -> 4개


from collections import Counter
def solution(clothes):
    answer = 1
    c = [x[1] for x in clothes]
    d = Counter(c)
    for v in d.values():
        answer = answer * (v+1) #3
    return answer-1