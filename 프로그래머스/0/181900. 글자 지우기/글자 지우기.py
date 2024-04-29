def solution(my_string, indices):
    arr = [x for x in my_string]
    answer = ''
    for i in range(len(arr)):
        if i not in indices:
            answer += arr[i]
    return answer