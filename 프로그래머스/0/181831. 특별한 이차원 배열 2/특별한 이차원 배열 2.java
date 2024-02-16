class Solution {
    public int solution(int[][] arr) {
        int answer = 0;
        
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j ++) {
                if (arr[i][j] == arr[j][i]) {
                    answer += 1;
                } else {
                    answer += 0;
                }
            }
        }
        
        if (answer == arr.length*arr.length) {
            return 1;
        } else{
            return 0;
        }
    }
}