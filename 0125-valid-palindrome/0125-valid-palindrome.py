class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = [c.lower() for c in s if c.isalnum()]

        for i in range(len(letters)):
            if letters[i] != letters[len(letters)-i-1]:
                return False

        return True

        