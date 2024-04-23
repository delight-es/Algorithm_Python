def solution(num_list):
    A, B = sum(num_list[0::2]), sum(num_list[1::2])
    return A if A>B else B