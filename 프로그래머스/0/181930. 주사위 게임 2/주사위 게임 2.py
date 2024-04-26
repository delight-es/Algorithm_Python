def solution(a, b, c):
    answer = a+b+c
    if (a == b == c):
        answer *= ((a**2)*3) * ((a**3)*3)
    elif (a == b) or (b == c) or (a == c):
        answer *= (a**2 + b**2 + c**2)
    return answer