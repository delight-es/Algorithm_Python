def solution(myString):
    arr = [m for m in myString]
    for i in range(len(myString)):
        if arr[i] < 'l':
            arr[i] = 'l'
    return ''.join(arr)