def solution(quiz):
    answer = []
    for q in quiz:
        list = q.split(" ")
        a, b, cal, res = list[0], list[2], list[1], int(list[4])
        if(eval(f"{a} {cal} {b}") == res):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer