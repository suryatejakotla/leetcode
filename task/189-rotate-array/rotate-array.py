class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # To handle cases where k is larger than the array length
        nums[:] = nums[-k:] + nums[:-k]

        