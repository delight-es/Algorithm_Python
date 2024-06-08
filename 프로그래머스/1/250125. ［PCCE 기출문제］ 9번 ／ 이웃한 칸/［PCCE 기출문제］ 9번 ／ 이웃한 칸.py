def solution(board, h, w): # 보드, 선택한 x좌표, 선택한 y좌표
    x,y = h,w
    color, answer = board[h][w], 0 # 색상, 시작좌표, 정답
    pos = [[1,0], [-1,0], [0,1], [0,-1]] # 상하좌우
    
    for p in pos:
        now_x, now_y = x+p[0], y+p[1]
        if now_x < 0 or now_y < 0 or now_x >= len(board) or now_y >= len(board):
            pass
        else:
            if color == board[now_x][now_y]:
                answer += 1
    return answer