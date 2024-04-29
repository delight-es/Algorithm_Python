def solution(strArr):
    lenArr = [len(x) for x in strArr]
    arr = [0 for _ in range(30)]
    for i in lenArr:
        arr[i-1] += 1
    return max(arr)