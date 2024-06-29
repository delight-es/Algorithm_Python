lst = [int(input()) for _ in range(9)]
lst.sort()
#print(lst)

# 전체 키 총합에서 두명의 키를 뺐을 때 키가 100이면 됨
total = 0
for i in range(9):
    total += lst[i]
#print(total)

is_end = False
# for loop 두번 돌려서 전체에서 2개 뺏을 때 키가 100인지?
for x in range(9):
    for y in range(9):
        if x==y:
            continue
        
        if (total-(lst[x]+lst[y])) == 100:
            #print(x, y)
            lst.remove(lst[y])
            lst.remove(lst[x])
            is_end = True
            break
    if is_end == True:
        break

for num in lst:
    print(num)