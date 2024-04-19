def solution(myString, pat):
    myString = myString.replace('A', 'X')
    myString = myString.replace('B', 'Y')
    myString = myString.replace('X', 'B')
    myString = myString.replace('Y', 'A')
    return 1 if pat in myString else 0

