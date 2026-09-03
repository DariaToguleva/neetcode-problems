class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        end = 0

        for num in sets:
            if (num - 1) not in sets:
                leng = 1
                while (num + leng) in sets:
                    leng += 1
                end = max(end, leng)

        return end            