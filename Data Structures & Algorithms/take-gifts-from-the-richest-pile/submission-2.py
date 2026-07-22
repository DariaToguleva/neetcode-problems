import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-n for n in gifts]
        heapq.heapify(maxHeap)
        
        for i in range(k):
            maxi = math.floor(math.sqrt(-heapq.heappop(maxHeap)))
            heapq.heappush(maxHeap, -maxi)
            print(maxi)
        print(maxHeap)
        return int(abs(sum(maxHeap)))