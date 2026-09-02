class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 10
        temp = 0
        n = num
        while result > 9:
            while n != 0:
                temp += n % 10
                n //= 10
            result = temp
            n = temp
            temp = 0

        return result

        
        