class Solution {
    public int trap(int[] height) {
        int i = 0;
        int maxLeft = height[i];

        int j = height.length - 1;
        int maxRight = height[j];

        int sum = 0;
        while (i < j) {
            if (maxLeft < maxRight) {
                i++;
                maxLeft = Math.max(maxLeft, height[i]);
                sum += maxLeft - height[i];
            } else {
                j--;
                maxRight = Math.max(maxRight, height[j]);
                sum += maxRight - height[j];
            }
        }
        return sum;    
    }
}
