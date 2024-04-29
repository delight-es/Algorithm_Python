def solution(myString, pat):
    f = myString[::-1].find(pat[::-1])
    return myString[:len(myString)-f]