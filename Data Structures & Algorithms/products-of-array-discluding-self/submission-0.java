class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] fin = new int[nums.length];

        fin[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            fin[i] = fin[i - 1] * nums[i - 1];
        }

        int post = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            fin[i] = fin[i] * post;
            post *= nums[i];
        }

        return fin;
    }
}  
