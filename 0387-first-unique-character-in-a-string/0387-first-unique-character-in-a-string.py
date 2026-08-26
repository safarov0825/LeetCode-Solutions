class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = Counter(s)

        for l in s:
            if seen[l] == 1:
                return s.index(l)

        return -1
        