class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        if word.isalnum() != True:
            return False
        else:
            vowel, consonant = False, False
            for c in word:
                if c.lower() in 'aeiuo':
                    vowel = True
                elif c.isalpha():
                    consonant = True
        
        return (vowel and consonant) == True

        