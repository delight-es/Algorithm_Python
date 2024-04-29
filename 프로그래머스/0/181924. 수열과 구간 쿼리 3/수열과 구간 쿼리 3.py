def solution(arr, queries):
    temp = 0
    for i,j in queries:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
    return arr