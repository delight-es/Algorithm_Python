def solution(arr):
    str_idx, end_idx = 0,0
    for i in range(len(arr)):
        if arr[i] == 2:
            str_idx = i
            break
    for j in range(len(arr)-1,0,-1):
        if arr[j] == 2:
            end_idx = j
            break
    return [-1] if (str_idx == end_idx == 0) else arr[str_idx:end_idx+1]