def solution(s):
    lst = []
    for i in s:
        if i == '(':
            lst.append('(')
        else:
            try:
                lst.pop()
            except IndexError:
                return False
    return len(lst)== 0