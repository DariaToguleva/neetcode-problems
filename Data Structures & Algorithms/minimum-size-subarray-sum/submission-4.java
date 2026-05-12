class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        if(nums[0] >= target){
            return 1;
        }
        int l = 0;
        int res = 0;
        int sum = nums[0];

        for(int r = 1; r < nums.length; r++){
            sum += nums[r];
            while(sum >= target){
                if(Math.min(res, r-l+1) == 0){
                    res = r - l + 1;
                } else {
                    res = Math.min(res, r - l + 1);
                }
                if(r == l){
                    return 1;
                }
                l++;
                sum -= nums[l - 1];
            }
            System.out.print(r + " ");
            System.out.print(l + " ");
            System.out.println(res);
            
        }

        return res;
    }
}