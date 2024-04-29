def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        answer.extend([int(i[s:s+l])])
    return [x for x in answer if x > k]