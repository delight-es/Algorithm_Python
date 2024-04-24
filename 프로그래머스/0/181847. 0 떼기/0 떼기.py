def solution(n_str):
    while n_str.startswith('0'):
        n_str = n_str[1:]
    return n_str