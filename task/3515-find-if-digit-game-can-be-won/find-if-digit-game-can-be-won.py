class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        k=0
        s=0
        for i in range(len(nums)):
            if nums[i]<=9:
                k+=nums[i]
            else:
                s+=nums[i]
        return k!=s

