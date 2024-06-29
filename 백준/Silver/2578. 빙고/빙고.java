import java.util.*;
import java.io.*;

/* 빙고 
 * arr: 빙고배열(2차원-1~25), say: 부른숫자배열(1차원)
 * (분석) 시뮬레이션
 */

public class Main {
    static int arr[][] = new int[5][5], say[] = new int[25], cnt = 0;
    static boolean checkRow[] = new boolean[5];
    static boolean checkCol[] = new boolean[5];
    static boolean checkDiag1 = false;
    static boolean checkDiag2 = false;
    
    static boolean find(int x, int y) { //지금 갱신한 val의 행열에 대해서만
        boolean bingo = false;
        
        //1) 해당 행 모두 맞췄는지 확인
        if (!checkRow[x]) {
            boolean rowBingo = true;
            for (int i = 0; i < 5; i++) {
                if (arr[x][i] != 0) {
                    rowBingo = false;
                    break;
                }
            }
            if (rowBingo) {
                checkRow[x] = true;
                bingo = true;
                cnt++;
            }
        }
        
        //2) 해당 열 모두 맞췄는지 확인
        if (!checkCol[y]) {
            boolean colBingo = true;
            for (int i = 0; i < 5; i++) {
                if (arr[i][y] != 0) {
                    colBingo = false;
                    break;
                }
            }
            if (colBingo) {
                checkCol[y] = true;
                bingo = true;
                cnt++;
            }
        }
        
        //3) 대각선 원소에 해당하면 해당 대각선 모두 맞췄는지 확인
        //왼쪽 대각선 (0,0) (1,1) (2,2) (3,3) (4,4)
        if (x == y && !checkDiag1) {
            boolean diag1Bingo = true;
            for (int i = 0; i < 5; i++) {
                if (arr[i][i] != 0) {
                    diag1Bingo = false;
                    break;
                }
            }
            if (diag1Bingo) {
                checkDiag1 = true;
                bingo = true;
                cnt++;
            }
        }
        
        //오른쪽 대각선 (0,4) (1,3) (2,2) (3,1) (4,0)
        if (x + y == 4 && !checkDiag2) {
            boolean diag2Bingo = true;
            for (int i = 0; i < 5; i++) {
                if (arr[i][4 - i] != 0) {
                    diag2Bingo = false;
                    break;
                }
            }
            if (diag2Bingo) {
                checkDiag2 = true;
                bingo = true;
                cnt++;
            }
        }
        
        return bingo;
    }

    static void bingo(int idx, int val) { //인덱스,값
        int x = -1, y = -1;
        //1) 부른 숫자 지우기
        outer: for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[i][j] == val) { //부르면 0으로 체크
                    arr[i][j] = 0;
                    x = i;
                    y = j;
                    break outer;
                }
            }
        }

        //2) 빙고인지 확인하고 빙고면 cnt+1
        find(x, y);

        //3) 빙고 3개 모았으면 외치고 종료
        if (cnt >= 3) {
            System.out.println(idx + 1);
            System.exit(0); // 프로그램 종료
        }
    }
    
    public static void main(String[] args) throws Exception {
        //1. 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) arr[i][j] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) say[(5 * i) + j] = Integer.parseInt(st.nextToken());
        }
        cnt = 0;

        //2. 처리
        for (int s = 0; s < say.length; s++) {
            bingo(s, say[s]); //idx,val
        }
        
        //3. 출력
        br.close();
    }
}
