for t in range(1, 11):
    n, lst = input().split()
    lst = [l for l in lst]
    i = 0
    while i <= len(lst)-2:
        if lst[i] == lst[i+1]:
            lst.pop(i)
            lst.pop(i)
            i -= 2
        i += 1

    print(f"#{t} {''.join(lst)}")