class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        total = 0

        try:
            for n in reversed(nums):
                nums.remove(0)
                nums.append(0)
        except ValueError:
            pass

        