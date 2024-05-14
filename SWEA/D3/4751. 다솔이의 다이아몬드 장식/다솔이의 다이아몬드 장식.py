T = int(input())

for t in range(1,T+1):
    eng = input()
    arr = []

    # 꾸미기
    for i in range(5):
        # 첫, 다섯번째 줄
        if i == 0 or i==4:
            line = '..' + '#...'*(len(eng)-1) + '#..'
        # 두, 네번째 줄
        elif i == 1 or i == 3:
            line = '.' + '#.'*(len(eng)*2)
        # 세번째 줄
        elif i == 2:
            line = '#'
            for e in eng:
                line += '.'+e+'.#'
        arr.append([line])

    for i in range(len(arr)):
        print(arr[i][0])