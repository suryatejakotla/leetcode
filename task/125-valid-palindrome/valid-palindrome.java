class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase().replaceAll("[^a-z0-9]","");
        char[] charArray = s.toCharArray();
        int k=0;
        int r = charArray.length-1;
        while(k<r)
        {
            if(charArray[k]!=charArray[r])
            {
                return false;
            }
            k++;
            r--;
        }
        return true;
    }
}