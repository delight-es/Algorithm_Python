def solution(my_string):
    return sorted([my_string[i:len(my_string)] for i in range(len(my_string))])