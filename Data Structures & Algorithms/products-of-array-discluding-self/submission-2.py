class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        right = 1
        for j in range(len(nums) - 1, 0, -1):
            left[j] = left[j] * right
            right = right * nums[j]

        left[0] = right
        return left
