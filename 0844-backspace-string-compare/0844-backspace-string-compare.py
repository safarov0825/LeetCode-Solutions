class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stackfors = []
        stackfort = []

        for c in s:
            if c == "#":
                if stackfors:
                    stackfors.pop()
            else:
                stackfors.append(c)

        for c in t:
            if c == "#":
                if stackfort:
                    stackfort.pop()
            else:
                stackfort.append(c)

        return stackfors == stackfort
        