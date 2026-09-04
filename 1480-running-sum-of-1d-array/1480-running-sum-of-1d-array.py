class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = [0]

        for n in nums:
            sums.append(sums[-1] + n)

        sums.pop(0)
        return sums
        