class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        valid = []

        for n in nums:
            if n in seen:
                valid.remove(n)
                pass
            else:
                valid.append(n)
            seen.add(n)

        return valid[0]

        
        