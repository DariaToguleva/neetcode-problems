class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = {}

        for num in nums:
            one[num] = one.get(num, 0) + 1
        for val in one:
            if one[val] == 1:
                return val