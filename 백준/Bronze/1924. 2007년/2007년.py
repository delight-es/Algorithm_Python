day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day_total = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mm, dd = map(int, input().split())
total_num = dd #일수 더하고
if (mm > 1): #2월부터
    for i in range(mm):
        total_num += day_total[i] #달도 더함

print(day[total_num % 7])