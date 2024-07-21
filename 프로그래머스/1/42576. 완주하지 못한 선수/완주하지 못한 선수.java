import java.io.*;
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
		//1. 해시 생성
        HashMap<String, Integer> h = new HashMap<>();
        for(String p:participant) h.put(p, h.getOrDefault(p, 0)+1);
      
        //2. 있는 선수 제거
        for(String c:completion) h.replace(c, h.get(c)-1);
        
        //3. 남은 선수 출력
        for(String p:participant) {
        	if(h.get(p)!=0) answer=p;
        }
        return answer;
    }
}