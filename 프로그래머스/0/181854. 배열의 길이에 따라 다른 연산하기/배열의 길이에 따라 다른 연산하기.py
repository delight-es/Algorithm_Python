def solution(arr, n):
    answer = arr
    N = len(arr)
    if N % 2: #길이-홀수
        for i in range(0, N, 2): #짝수
            answer[i] += n
    else: #길이-짝수
        for i in range(1, N, 2): #홀수
            answer[i] += n
    return answer