class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0  # If there are 4 or fewer elements, the difference will always be 0

        nums.sort()
        return min(
            nums[-1] - nums[3],  # Option 1: Keep the first three elements unchanged
            nums[-2] - nums[2],  # Option 2: Change the first element to the fourth smallest
            nums[-3] - nums[1],  # Option 3: Change the second element to the fifth smallest
            nums[-4] - nums[0],)