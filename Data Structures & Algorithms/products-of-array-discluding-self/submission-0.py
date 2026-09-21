class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lis = []
        prod = 1
        for i in range(len(nums)):
            lis.append(prod)
            prod = prod * nums[i]

        prod = 1
        for j in range(len(nums) - 1, -1, -1):
            lis[j] = lis[j] * prod
            prod = prod * nums[j]

        return lis