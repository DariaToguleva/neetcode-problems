from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        arr = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums)

        for num, count in freq.items():
            arr[count].append(num) 

        for count in range(len(arr) - 1, 0, -1):
            for num in arr[count]:
                res.append(num)
                if len(res) == k:
                    return res
        return res        