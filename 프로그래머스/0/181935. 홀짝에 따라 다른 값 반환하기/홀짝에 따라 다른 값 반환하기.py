def solution(n):
    return sum([i for i in range(1,n+1,2)]) if n%2==1 else sum([i**2 for i in range(0,n+1,2)])