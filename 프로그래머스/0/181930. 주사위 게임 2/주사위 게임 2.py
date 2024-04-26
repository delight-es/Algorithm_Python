def solution(a, b, c):
    if a == b == c:
        score = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or b == c or a == c:
        score = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        score = a + b + c
    return score
