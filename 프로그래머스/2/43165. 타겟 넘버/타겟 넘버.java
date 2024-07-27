class Solution {
    static int answer=0;
	static int[] a; 
	static boolean[] v;
	
	static void sub(int cnt, int sum, int target, int N) {
		if(cnt == N) {
			if(sum==target) answer++; 
			return;
		}
		v[cnt] = true;
		sub(cnt+1, sum+a[cnt], target, N);
		v[cnt] = false;
		sub(cnt+1, sum-a[cnt], target, N);
	}
    
	public static int solution(int[] numbers, int target) {
        a = numbers;
        v = new boolean[numbers.length];
        sub(0, 0, target, numbers.length);
        return answer;
    }
}