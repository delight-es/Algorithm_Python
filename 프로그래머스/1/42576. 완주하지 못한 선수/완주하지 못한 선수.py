from collections import Counter
def solution(participant, completion):
    p, c = Counter(participant), Counter(completion)
    answer = p-c
    return list(answer.keys())[0]