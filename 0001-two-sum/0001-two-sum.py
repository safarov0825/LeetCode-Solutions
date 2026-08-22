class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_target = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == new_target:
                    return [i, j]