class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()

        def dfs(i, r):
            if r == 0:
                res.append(sub.copy())
                return
            if i >= len(candidates) or r < 0:
                return

            sub.append(candidates[i])    
            dfs(i + 1, r - candidates[i])
            sub.pop()

            j = i + 1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            dfs(j, r)

        dfs(0, target)
        return res        