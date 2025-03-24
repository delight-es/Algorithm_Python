def solution(babbling):
    say = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    # 각 리스트별
    for b in babbling:
        word = b
        # 각 발음별
        for s in say:
            if(s in word):
                word = word.replace(s, " ")
        # 다 돌았으면 갱신
        if(word.strip() == ""): 
            answer += 1
    
    return answer