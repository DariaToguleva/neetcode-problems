class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        lists = []
        used = [False] * len(nums)

        def dfs():
            if len(lists) == len(nums):
                res.append(lists.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True        
                lists.append(nums[i])
                dfs()

                lists.pop()
                used[i] = False    
        dfs()
        return res    
            
