def solution(order):
    total = 0
    for i in order:
        total += 4500
        if 'cafelatte' in i:
            total += 500
    return total