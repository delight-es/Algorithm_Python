def solution(a, d, included):
    arr = [i for i in range(a, (len(included)-1)*d+1+a, d)]
    return sum([arr[x] for x in range(len(included)) if included[x] == True])
