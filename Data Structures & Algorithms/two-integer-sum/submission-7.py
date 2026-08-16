class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapP = {}

        for index, val in enumerate(nums):
            difference = target - val
            if difference in mapP:
                return [mapP[difference], index]
            mapP[val] = index    