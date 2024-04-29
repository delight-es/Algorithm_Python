def solution(my_string, indices):
    return ''.join([j for i, j in enumerate(my_string) if i not in indices])
    