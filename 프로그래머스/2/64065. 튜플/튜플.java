import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        // 가장 앞의 {{ 를 제거
        s = s.substring(2, s.length() - 2);
        // 가장 뒤의 }} 를 제거한 뒤, },{ 형태의 문자열을 -로 바꾸기
        s = s.replace("},{", "-");
        // 위에서 바꾼 문자열을 기준으로 split 하기
        String[] str = s.split("-");
        // 나눠진 문자열 배열을 길이에 따라 다시 정렬
        Arrays.sort(str, new Comparator<String>() {
            public int compare(String o1, String o2) {
                return Integer.compare(o1.length(), o2.length());
            }
        });

        // 각 문자열 탐색
        for (String x : str) {
            // 한 문자열마다 ,를 기준으로 split하여 새로운 배열 만들기
            String[] temp = x.split(",");
            // 새로 만든 문자열 배열에는 정수값만 존재하며 이를 탐색
            for (int i = 0; i < temp.length; i++) {
                // 각 문자열 값을 정수로 바꾸기
                int n = Integer.parseInt(temp[i]);
                // 튜플에 들어있는 값이 아니라면 추가해주기
                if (!answer.contains(n)) {
                    answer.add(n);
                }
            }
        }
        return answer;
    }
}
