class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        total = 0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                newval=nums[i-1]+1
                total+=newval-nums[i]
                nums[i]=newval
        return total
        