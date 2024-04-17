def solution(arr1, arr2):
    answer = 0
    A = len(arr1)
    B = len(arr2)
    
    if A > B: answer = 1
    elif A < B: answer = -1
    else: #A == B
        sum_A, sum_B = 0, 0
        for i in arr1: sum_A += i
        for j in arr2: sum_B += j
        if sum_A > sum_B: answer = 1
        elif sum_A < sum_B : answer = -1
        else: answer = 0
    return answer