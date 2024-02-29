import sys

num = int(sys.stdin.readline())
for i in range(1,num+1):
    A,B = map(int,sys.stdin.readline().split())
    print('Case #'+str(i)+': '+str(A)+' + '+str(B)+' = '+str(A+B))