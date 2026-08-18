class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = sumi = 0
        mapP = {0:1}

        for num in nums:
            sumi += num
            diff = sumi - k
            res += mapP.get(diff, 0)
            mapP[sumi] = 1 + mapP.get(sumi, 0)
        return res    