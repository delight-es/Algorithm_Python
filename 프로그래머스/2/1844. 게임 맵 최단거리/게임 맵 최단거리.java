import java.util.*;
import java.io.*;

/* 게임맵최단거리
 * 시작점(1,1) ~ 끝점(n,m)으로 우좌하상(동서남북) 이동
 * arr 배열: 0(벽-검정), 1(길-흰색)
 * 가장 지나는 최소 칸수 --> 출력! (단, 도착 못하면 -1)
 * (분석) 최단거리 => BFS
 */

class Solution {
	//우좌하상
	static int[] di = {0,0,1,-1};
	static int[] dj = {1,-1,0,0};
	static int N=0, M=0; //배열크기
	static int[][] arr; //배열
	static boolean[][] v; //방문처리
	
	static void bfs(int i, int j, int cnt) {
		ArrayDeque<int[]> q = new ArrayDeque<>();
		v[i][j] = true; //방문처리
		q.offer(new int[] {i,j,cnt}); //큐 넣기
		while(!q.isEmpty()) {
			int[] ij = q.poll(); //꺼내서
			i = ij[0];
			j = ij[1];
            int c = ij[2];
            //처리
            arr[i][j] = c;
			for(int d=0; d<4; d++) { //새 좌표 탐색
				int ni = i+di[d];
				int nj = j+dj[d];
                int nc = c+1;
				//범위 정상 + 방문 X + 길이면
				if (0<=ni && ni<N && 0<=nj && nj<M && !v[ni][nj] && arr[ni][nj]==1) {
					v[ni][nj] = true; //방문처리
					arr[ni][nj] += arr[i][j]; //이전이동+1
					q.offer(new int[] {ni,nj,nc}); //큐에 넣기
				}
			}
		}
	}
	
	static int solution(int[][] maps) {
		//1. 입력
		for(int[] m:maps) System.out.println(Arrays.toString(m));
		arr = maps;
		N = maps.length;
		M = maps[0].length;
		v = new boolean[N][M];
		//2. 처리
		bfs(0,0,1);
		System.out.println();
		for(int[] m:arr) System.out.println(Arrays.toString(m));
		
		int answer = arr[N-1][M-1]<=1? -1 : arr[N-1][M-1];
		return answer;
    }
}
