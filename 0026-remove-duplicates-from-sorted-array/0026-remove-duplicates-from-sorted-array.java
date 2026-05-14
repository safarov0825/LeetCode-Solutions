class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1;
        int num = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == num) continue;
            num = nums[i];
            nums[count] = nums[i];
            count++;
        }

        return count;
    }
}