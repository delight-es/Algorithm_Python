big = [1,3,5,7,8,10,12]
small = [4,6,9,11]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

i=1
dd=0
m, d = map(int,input().split())

for i in range(1,m):
    if i == 2:
        dd += 28
    elif i in big:
        dd += 31
    else:
        dd += 30

dd += d

print(week[(dd%7)-1])