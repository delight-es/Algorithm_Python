import java.io.*;
import java.util.*;

/* 체스판 다시 칠하기 
 * N: 세로크기, M: 가로크기 => 8*8 크기로 자르기
 * 상하좌우 전부 'W','B' 번갈아서 있어야함
 * 바꿔야하는 개수 최소 --> 출력
 * (경우의 수) 2개 >> 좌상단 'W' OR 'B'
 */

public class Main {
	static int min=Integer.MAX_VALUE;
	static char[][] arr;
	
	//(1) 새로운 8*8 배열 가져오기
	static char[][] sub(int i, int j) {
		char[][] c = new char[8][8]; //(0,0)~(8,8)
		int x_idx=0, y_idx=0; //idx
		for(int y=i; y<i+8; y++) {
			x_idx=0;
			for(int x=j; x<j+8; x++) {
				c[y_idx][x_idx] = arr[y][x]; x_idx++;
			}
			y_idx++;
		}
		return c;
	}
	
	// (2) 체크하기
	static int check(char[][] c) {
		int local=Integer.MAX_VALUE;
		char[] start = {'W', 'B'};
		for(int s=0; s<=1; s++) { //좌상단('W','B')
			int cnt = 0; char target = start[s]; 
			//8*8 돌면서
			for(int i=0; i<8; i++) {
				for(int j=0; j<8; j++) {
					boolean i_iseven=(i%2==0), j_iseven=(j%2==0);
					char now=c[i][j];
					if(i_iseven && j_iseven && now!=target) cnt++; //같아야함
					if(i_iseven && !j_iseven && now==target) cnt++; //달라야함
					if(!i_iseven && j_iseven && now==target) cnt++; //달라야함
					if(!i_iseven && !j_iseven && now!=target) cnt++; //같아야함
				}
			}
			local = Math.min(local, cnt);
		}
		return local;
	}
	
	public static void main(String[] args) throws Exception{
		//1. 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		arr = new char[N][M];
		for(int i=0; i<N; i++) {
			String s = br.readLine();
			for(int j=0; j<M; j++) arr[i][j] = s.charAt(j);
		}
		
		//2. 처리
		for(int i=0; i<=N-8; i++) {//세로
			for(int j=0; j<=M-8; j++) {//가로
				// (1) 새로운 8*8 배열 가져오기
				char[][] c = sub(i,j);
				// (2) 체크하기
				min = Math.min(check(c),min);
			}
		}
		
		//3. 출력
		System.out.println(min);
		br.close();
	}
}
