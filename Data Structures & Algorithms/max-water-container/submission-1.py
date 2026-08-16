class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        r, l = 0, len(heights) - 1

        while r <= l:
            area = min(heights[r], heights[l]) * (l - r)
            if area > maxi:
                maxi = area
            if heights[r] <= heights[l]:
                r += 1
            elif heights[r] > heights[l]:
                l -= 1
            print(area)    

        return maxi