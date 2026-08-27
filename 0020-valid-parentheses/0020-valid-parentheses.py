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
                if not par:
                    return False
                elif p == par[-1]:
                    par.pop()
                else:
                    return False
            
        if not par:
            return True
        return False
        