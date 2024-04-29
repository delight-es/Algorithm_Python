def solution(arr):
    pow, x = 1, len(arr)
    while pow < x:
        pow *= 2
    return arr+[0]*(pow-x)