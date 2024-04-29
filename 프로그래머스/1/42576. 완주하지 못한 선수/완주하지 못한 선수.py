from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    for i in p:
        if i not in c:
            return i
        else:
            if p[i] != c[i]:
                return i
    