def solution(angle):
    answer = 0

    # 예각
    if (0<angle) and (angle<90):
        answer = 1
    # 직각
    elif (angle == 90):
        answer = 2
    # 평각
    elif (angle == 180):
        answer = 4
    # 평각
    else:   
        answer = 3
    return answer