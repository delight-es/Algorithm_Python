def solution(date1, date2):
    if (date1[0] < date2[0]): #연도 작으면
        return 1
    elif (date1[0] == date2[0]): #연도 같으면
        if (date1[1] < date2[1]): #월 작으면
            return 1
        elif (date1[1] == date2[1]): #월 같으면
            if (date1[2] < date2[2]): #일 작으면
                return 1
    return 0