from math import prod
def solution(num_list):
    return 1 if prod(num_list) < sum(num_list)**2 else 0