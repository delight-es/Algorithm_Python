def solution(arr, k):
    return [i*k for i in arr] if k%2==1 else [i+k for i in arr]