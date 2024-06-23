class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_values = []  # To store maximum values
        min_values = []  # To store minimum values
        left = 0
        max_length = 0

        for right in range(len(nums)):
        # Update max_values
            while max_values and nums[right] > max_values[-1]:
                max_values.pop()
            max_values.append(nums[right])

        # Update min_values
            while min_values and nums[right] < min_values[-1]:
                min_values.pop()
            min_values.append(nums[right])

        # Check if the difference exceeds the limit
            while max_values[0] - min_values[0] > limit:
                if max_values[0] == nums[left]:
                    max_values.pop(0)
                if min_values[0] == nums[left]:
                    min_values.pop(0)
                left += 1

        # Update max_length
            max_length = max(max_length, right - left + 1)

        return max_length