# 1번째 방법
All = input()
num = len(All)
for i in range(0,num,10):
    print(All[i:i+10])

# 2번째 방법
All = input()
num = len(All)
for i in range(1, num+1):
    if (i > 0 and i % 10 == 0):
        print(All[i - 10:i])
    else:
        if (i==num):
            print(All[num//10*10 : i+1])
