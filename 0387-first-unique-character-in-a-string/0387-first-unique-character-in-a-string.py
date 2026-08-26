class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)

        for i, l in enumerate(s):
            if count[l] == 1:
                return i

        return -1
        