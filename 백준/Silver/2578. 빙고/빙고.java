import java.util.*;
import java.io.*;

/* 빙고 
 * arr: 빙고배열(2차원-1~25), say: 부른숫자배열(1차원)
 * (분석) 시뮬레이션
 * (!) 한 값을 지우면서 빙고는 각 행,열,대각선에 대해 동시에 여러번 발생 O
 */

public class Main {
	static int arr[][]=new int[5][5], 
	say[]=new int[25], cnt=0;

	//[1] 부른 숫자 지우기
	static void delete(int val) {
		int x=10, y=10;
		exit: for(int i=0; i<5; i++) {
			for(int j=0; j<5; j++ ) {
				if(arr[i][j] == val) { //부르면 0으로 체크
					arr[i][j] = 0;
					x=i;
					y=j;
					check(x,y,val);
					break exit;
				}
			}
		}
	}
	
	//[2] 빙고 가능한지 확인
	static void check(int x, int y, int val) { //지금 갱신한 값에 대해서만
		//1) 해당 행 모두 맞췄는지 확인
		int sum = 0;
		for(int i=0; i<5; i++) sum += arr[x][i];
		if(sum == 0) cnt++;
		
		//2) 해당 열 모두 맞췄는지 확인
		sum = 0;
		for(int i=0; i<5; i++) sum += arr[i][y];
		if(sum == 0) cnt++;
		
		//3) 대각선 원소에 해당하면 해당 대각선 모두 맞췄는지 확인
		sum = 0;
		if (x==y) { //왼쪽 대각선 (0,0) (1,1) (2,2) (3,3) (4,4)
			for(int i=0; i<5; i++) sum += arr[i][i];
			if(sum == 0) cnt++;
		}
      
		sum = 0;
		if(x+y==4) { //오른쪽 대각선 (0,4) (1,3) (2,2) (3,1) (4,0)
			for(int i=0; i<5; i++) sum += arr[i][4-i];
			if(sum == 0) cnt++;
		}
	}	
	
	public static void main(String[] args) throws Exception{
		//1. 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for(int i=0; i<5; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<5; j++) arr[i][j] = Integer.parseInt(st.nextToken());
		}
		for(int i=0; i<5; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<5; j++) say[(5*i)+j] = Integer.parseInt(st.nextToken());
		}
		cnt=0;
		
		//2. 처리
        for (int s = 0; s < say.length; s++) {
            delete(say[s]);
            if (cnt >= 3) {  //빙고 3개 넘으면
                System.out.println(s+1);
                break; //종료
            }
        }
        
		//3. 출력
		br.close();
	}
}
