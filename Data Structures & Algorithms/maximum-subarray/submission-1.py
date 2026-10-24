class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        if len(nums) == 1:
            return max_sum
        for i in range(1, len(nums)):
            cur_sum += nums[i]
            if nums[i] > cur_sum:
                cur_sum = nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
