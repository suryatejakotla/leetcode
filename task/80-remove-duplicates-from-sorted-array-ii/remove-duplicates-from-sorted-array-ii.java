class Solution {
    public int removeDuplicates(int[] nums) {
        int x=1;
        for(int i =1; i<nums.length;i++)
        {
            if(x==1||nums[i]!=nums[x-2])
            {
                nums[x]=nums[i];
                x+=1;
            }
        }
        return x;
    }
}