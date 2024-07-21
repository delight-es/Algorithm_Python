import java.io.*;
import java.util.*;

/* 전화번호 목록
 * phone_book: 전화번호 적힌 명단
 * (분석 1) 정렬 -> 인접 접두사 확인[startsWith]
 * (분석 2) 해시[번호,인덱스] -> 해시 키에 있는지 확인[h.containsKey]
 */

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        /* (분석 1) 정렬 -> 인접 접두사 확인[startsWith] 
          // (1) 정렬
        Arrays.sort(phone_book);
          // (2) 앞뒤 원소 접두사 검사
        for (int i=0; i<phone_book.length-1; i++) {
            if(phone_book[i+1].startsWith(phone_book[i])) {// i가 j의 접두사면
                answer = false;
                break;
            }
        } */

        /* (분석 2) 해시[번호,인덱스] -> 해시 키에 있는지 확인[h.containsKey] */
          // (1) 해시 생성
        HashMap<String, Integer> h = new HashMap<>();
        for(int i=0; i<phone_book.length; i++) h.put(phone_book[i], i);
          // (2) 해시 키에 있는지 확인
        exit: for(int i=0; i<phone_book.length; i++) {
            for(int j=0; j<phone_book[i].length(); j++) {
                if(h.containsKey(phone_book[i].substring(0, j))) {
                    answer = false;
                    break exit;
                }
            }
        }
        return answer;
    }
}