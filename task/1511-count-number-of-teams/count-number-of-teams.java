class Solution {
    public int numTeams(int[] rating) {
        int n = rating.length;
        int count = 0;
        
        for (int j = 1; j < n - 1; j++) {
            int lessLeft = 0, moreLeft = 0;
            int lessRight = 0, moreRight = 0;
            
            for (int i = 0; i < j; i++) {
                if (rating[i] < rating[j]) {
                    lessLeft++;
                } else if (rating[i] > rating[j]) {
                    moreLeft++;
                }
            }
            
            for (int k = j + 1; k < n; k++) {
                if (rating[k] < rating[j]) {
                    lessRight++;
                } else if (rating[k] > rating[j]) {
                    moreRight++;
                }
            }
            
            count += lessLeft * moreRight + moreLeft * lessRight;
        }
        
        return count;
    }
}