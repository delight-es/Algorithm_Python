def solution(arr):
    pow = [2**x for x in range(0,11) if 2**x <= 1024]
    print(pow)
    x, zero = len(arr), 0
    
    for i in pow:
        if x <= i: #입력 <= 2 거듭제곱 리스트 원소
            zero = i
            break
            
    arr += [0]*(zero-x)
    return arr


