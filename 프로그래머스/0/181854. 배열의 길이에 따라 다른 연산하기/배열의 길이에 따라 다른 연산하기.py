def solution(arr, n):
    answer = arr
    if len(arr) % 2 == 1: # 길이-홀수
        for i in range(0, len(arr), 2): #짝수
            answer[i] += n
    else: # 길이-짝수
        for j in range(1, len(arr), 2): #홀수
            answer[j] += n
    return answer