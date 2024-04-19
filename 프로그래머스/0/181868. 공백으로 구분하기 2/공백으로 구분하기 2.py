def solution(my_string):
    answer = my_string.strip().split(' ')
    return [i for i in answer if i != '']