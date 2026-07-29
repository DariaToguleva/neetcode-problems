class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        d = dict()

        for num in nums:
            if d.get(num) != 1:
                d[num] = 1
            else:
                return True
        return False        
