import java.io.*;
import java.util.*;

/* 타겟 넘버
 * [입력] numbers : 사용할 수 있는 숫자
 * 		 target : 타겟 넘버
 * [출력] 타겟 넘버 만드는 방법 수
 * [분석] 재귀 --> target 값 찾을 때까지 더하고 빼서 다시 호출
 */

public class Solution {
	static int[] arr;
    static int N,answer;
    
    static void dfs(int cnt, int sum, int tar) { //깊이, 합, 타겟넘버
        if(cnt == N) { //종료조건
            if (sum == tar) answer++;
            return;
        }
        dfs(cnt+1, sum+arr[cnt], tar); //깊이+1, 총합+자신
        dfs(cnt+1, sum-arr[cnt], tar); //깊이+1, 총합-자신
    }
    
	public int solution(int[] numbers, int target) {
        N = numbers.length;
        arr = numbers;
        dfs(0,0,target); //깊이-0, 총합-0, 타겟넘버
        return answer;
    }
}
