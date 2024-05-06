def solution(citations):
    c = sorted(citations, reverse=True)
    print(c)
    # 값이 h와 같거나 큰 원소 개수 >= h and (전체 개수 - 앞 개수) <= h:
    h = c[0]
    while h >= 0:
        num = len([x for x in c if x >= h])
        if num >= h and len(c)-num <= h:
            return h
        h -= 1
    
    
    
    
    
    
#     for i in range(len(c)):
#         h,num = c[i], i+1
#         print('개수', num, h)
#         if num >= h and len(c)-num <= h:
#             print('들어온', h, num)
#             return h
    
#     # 없었다면
#     h = c[-1]
#     while h >= 0:
#         h,num = h-1, len(c)
#         if num >= h:
#             return h
    
    
    
    
    # # 처음부터 원소 값과 인덱스를 비교해서 
    # for i in range(len(c)):
    #     # 개수 >= h & 남은 개수 <= h
    #     if i+1 >= c[i] and len(c)-(i+1) <= c[i]:
    #         print(i+1)
    #         return c[i]
    # return len(c)