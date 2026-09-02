class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapP = {}

        for ind, num in enumerate(nums):
            if target - num in mapP:
                return [mapP[target - num], ind]
            mapP[num] = ind    