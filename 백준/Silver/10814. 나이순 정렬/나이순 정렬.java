import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		//1.입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		String[][] s = new String[N][2];
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			s[i][0] = st.nextToken();
			s[i][1] = st.nextToken();
		}
		
		//2.처리
		Arrays.sort(s, (o1,o2) -> Integer.compare( Integer.parseInt(o1[0]), Integer.parseInt(o2[0]) ));
		
		//3.출력
		for(String[] ss:s) {
			for(String sss:ss) System.out.print(sss+" ");
			System.out.println();
		}
		br.close();
	}
}
