class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par = []

        for p in s:
            if p == "(":
                par.append(")")
            elif p == "[":
                par.append("]")
            elif p == "{":
                par.append("}")
            else:
                if not par or p != par[-1]:
                    return False
                else:
                    par.pop()
            
        if not par:
            return True
        return False
        