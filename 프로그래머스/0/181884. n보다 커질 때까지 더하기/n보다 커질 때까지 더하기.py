def solution(numbers, n):
    num_sum = 0
    for i in numbers:
        num_sum += i
        if num_sum > n:
            return num_sum