def solution(myString):
    answer = []
    for i in myString.split('x'):
        answer.append(len(i))
    return answer