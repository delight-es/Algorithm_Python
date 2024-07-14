import java.io.*;
import java.util.*;

/* 분해합
 * n:숫자, sum:각자릿수+본인숫자
 * min:정답
 * (분석) 생성자가 될 수 있는 범위로 구현해 확인
 */
public class Main {
	public static void main(String[] args) throws Exception {
		//1. 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int min=Integer.MAX_VALUE;
		for(int i=N-100; i<N; i++) {
			int sum=i;
			String s = Integer.toString(i);
			for(int j=0; j<s.length(); j++) sum+=Character.getNumericValue(s.charAt(j));
			if(sum==N) min=Math.min(min, i);
		}
		
		//2. 출력
		if (min==Integer.MAX_VALUE) System.out.println(0);
		else System.out.println(min);
	}
}
