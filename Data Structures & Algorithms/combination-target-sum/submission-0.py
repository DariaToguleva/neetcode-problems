class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i, r):
            if i >= len(nums):
                return
            
            if r == 0:
                res.append(sub.copy())
                return 

            if r < 0:
                return  

            sub.append(nums[i])
            dfs(i, r - nums[i])
            sub.pop()

            dfs(i + 1, r)

        dfs(0, target)
        return res    