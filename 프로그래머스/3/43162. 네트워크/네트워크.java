import java.util.*;
import java.io.*;

/* 네트워크
 * n: 컴퓨터수, computers: 연결정보배열
 * a[i][j]가 1이면? i-j 연결
 * (분석) DFS나 BFS로 탐색 --> 연결된 수 구하기
 */

class Solution {
    static ArrayList<Integer>[] arr;
	static boolean[] v;
	
	static void bfs(int i) {
		ArrayDeque<Integer> q = new ArrayDeque<>();
		v[i] = true;
		q.offer(i);
		while(!q.isEmpty()) {
			i = q.poll();
			//처리
			for(int ni:arr[i]) 
				if(!v[ni]) {
					v[ni] = true;
					q.offer(ni);
				}
		}
	}
	public static int solution(int n, int[][] computers) {
        int answer = 0;
        arr = new ArrayList[n+1]; //1-base
        v = new boolean[n+1];
        //1. 인접배열 설정
        for(int i=0; i<=n; i++) arr[i] = new ArrayList<Integer>();
        for(int i=0; i<n; i++) {
        	for(int j=0; j<n; j++) {
        		if(i==j) continue;
        		if(computers[i][j] == 1) arr[i+1].add(j+1); //단방향
        	}
        }
        //2. bfs
        for(int i=1; i<=n; i++) {
        	if(!v[i]) {
        		bfs(i); answer++;
        	}
        }
        return answer;
    }
}