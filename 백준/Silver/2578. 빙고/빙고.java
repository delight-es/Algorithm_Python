import java.util.*;
import java.io.*;

/* 빙고 
 * arr: 빙고배열(2차원-1~25), say: 부른숫자배열(1차원)
 * (분석) 시뮬레이션
 */

public class Main {
    static int arr[][] = new int[5][5], say[] = new int[25], cnt = 0;

    static boolean checkRow(int x) {
        for (int i = 0; i < 5; i++) {
            if (arr[x][i] != 0) return false;
        }
        return true;
    }

    static boolean checkCol(int y) {
        for (int i = 0; i < 5; i++) {
            if (arr[i][y] != 0) return false;
        }
        return true;
    }

    static boolean checkDiag1() {
        for (int i = 0; i < 5; i++) {
            if (arr[i][i] != 0) return false;
        }
        return true;
    }

    static boolean checkDiag2() {
        for (int i = 0; i < 5; i++) {
            if (arr[i][4 - i] != 0) return false;
        }
        return true;
    }

    static void bingo(int idx, int val) { // 인덱스, 값
        int x = -1, y = -1;
        // 1) 부른 숫자 지우기
        outer: for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[i][j] == val) { // 부르면 0으로 체크
                    arr[i][j] = 0;
                    x = i;
                    y = j;
                    break outer;
                }
            }
        }

        // 2) 빙고인지 확인하고 빙고면 cnt+1
        if (checkRow(x)) cnt++;
        if (checkCol(y)) cnt++;
        if (x == y && checkDiag1()) cnt++;
        if (x + y == 4 && checkDiag2()) cnt++;

        // 3) 빙고 3개 모았으면 외치고 종료
        if (cnt >= 3) {
            System.out.println(idx + 1);
            System.exit(0); // 프로그램 종료
        }
    }

    public static void main(String[] args) throws Exception {
        // 1. 입력
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

        // 2. 처리
        for (int s = 0; s < say.length; s++) {
            bingo(s, say[s]); // idx,val
        }

        // 3. 출력
        br.close();
    }
}
