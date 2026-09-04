class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        temp = sum(nums[:k])
        maximum = temp / float(k)

        for right in range(k, len(nums)):
            temp -= nums[right - k]
            temp += nums[right]

            maximum = max(maximum, temp / float(k))

        return maximum
        