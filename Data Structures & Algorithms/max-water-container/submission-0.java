class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int i = 0;
        int j = heights.length - 1;

        while (i < j) {
            int curr = (j - i) * Math.min(heights[i], heights[j]);
            if (heights[i] < heights[j]) {
                i++;
            } else if (heights[i] >= heights[j]) {
                j--;
            } if (curr > max) {
                max = curr;
            }
        }
        return max;
    }
}
