"""
타겟 넘버
 * numbers : 사용할 수 있는 숫자
 * target : 타겟 넘버
 * (분석) 재귀 --> target 값 찾을 때까지 더하고 빼서 다시 호출
"""

answer = 0

def dfs(cnt, total, target, numbers): #깊이, 합, 목표값, 숫자배열
    global answer
    if cnt == len(numbers): #종료조건
        if total == target: #목표값 찾으면
            answer += 1
        return
    dfs(cnt+1, total+numbers[cnt], target, numbers) #더하기
    dfs(cnt+1, total-numbers[cnt], target, numbers) #빼기

def solution(numbers, target):
    dfs(0, 0, target, numbers)
    return answer