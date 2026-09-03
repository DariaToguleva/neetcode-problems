class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [0] * len(nums)

        mult = 1
        for i in range(len(nums)):
            prod[i] = mult
            mult *= nums[i]
            

        mult = 1
        for j in range(len(nums) - 1, -1, -1):
            prod[j] = prod[j] * mult
            mult *= nums[j]

        return prod    