class Solution {
    static int minCnt = Integer.MAX_VALUE;
    static String[] w;
    static boolean[] v;

    private static void dfs(String current, String target, int cnt) {
        if (current.equals(target)) {
            minCnt = Math.min(minCnt, cnt); //기존보다 더 작을경우
            return;
        }

        for (int i = 0; i < w.length; i++) {
            if (!v[i]) {
                int diff = 0;
                for (int j = 0; j < current.length(); j++) {
                    if (current.charAt(j) != w[i].charAt(j)) {
                        diff++;
                    }
                }
                if (diff == 1) {
                    v[i] = true;
                    dfs(w[i], target, cnt + 1);
                    v[i] = false;
                }
            }
        }
    }

    public static int solution(String begin, String target, String[] words) {
        w = words;
        v = new boolean[words.length];

        boolean isTargetInWords = false;
        for (String word : words) {
            if (word.equals(target)) {
                isTargetInWords = true;
                break;
            }
        }

        if (!isTargetInWords) return 0;

        dfs(begin, target, 0);

        return minCnt == Integer.MAX_VALUE ? 0 : minCnt;
    }

    public static void main(String[] args) {
        int answer = solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log", "cog"});
        System.out.println(answer); // Expected output: 4
    }
}