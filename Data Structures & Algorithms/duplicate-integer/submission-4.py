class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapH = {}
        for num in nums:
            if mapH.get(num, 0) + 1 > 1:
                return True
            mapH[num] = mapH.get(num, 0) + 1
        return False     