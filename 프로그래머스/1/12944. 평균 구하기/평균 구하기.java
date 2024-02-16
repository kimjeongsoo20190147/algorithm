class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int val_sum = 0;
        
        for (int i = 0; i < arr.length; i++) {
            val_sum += arr[i];
        }
        
        answer = (double) val_sum / arr.length;
        return answer;
    }
}