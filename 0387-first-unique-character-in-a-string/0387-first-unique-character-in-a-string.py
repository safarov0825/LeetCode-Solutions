class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        for l in s:
            count[l] = count.get(l, 0) + 1

        for i, l in enumerate(s):
            if count[l] == 1:
                return i

        return -1
        