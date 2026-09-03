class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxR, maxL = 0, 0
        tot = 0

        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                tot += maxL - height[l]
                l += 1
            elif height[l] >= height[r]:
                maxR = max(maxR, height[r])
                tot += maxR - height[r]
                r -= 1

        return tot           