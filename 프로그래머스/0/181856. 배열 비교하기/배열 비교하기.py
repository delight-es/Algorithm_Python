def solution(arr1, arr2):
    answer = 0
    A, B = len(arr1), len(arr2)
    if (A > B): answer = 1
    elif (A < B): answer = -1
    else:
        sum_A, sum_B = 0, 0
        for i in range(A):
            sum_A += arr1[i]
        for j in range(B):
            sum_B += arr2[j]
        if (sum_A > sum_B): answer = 1
        elif (sum_A < sum_B): answer = -1
        else: answer = 0
    return answer





