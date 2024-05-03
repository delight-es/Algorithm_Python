def solution(arr):
    answer = [arr[0]]
    for x in range(1, len(arr)):
        if arr[x] != answer[-1]:
            answer.append(arr[x])
    return answer