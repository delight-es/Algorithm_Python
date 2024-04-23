def prod(num_list):
    res = num_list[0]
    for i in range(1, len(num_list)):
        res *= num_list[i]
    return res

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else prod(num_list)