def solution(order):
    plus_menu = ['cafelatte', 'hotcafelatte', 'cafelattehot', 'icecafelatte', 'cafelatteice']
    total = 0
    for i in order:
        total += 4500
        if i in plus_menu:
            total += 500
    return total