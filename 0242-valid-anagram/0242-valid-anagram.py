class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counts, countt = {}, {}
        for l in s:
            counts[l] = counts.get(l, 0) + 1
        for l in t:
            countt[l] = countt.get(l, 0) + 1

        if counts == countt:
            return True
        return False
        