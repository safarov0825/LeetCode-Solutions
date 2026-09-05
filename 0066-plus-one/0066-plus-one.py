class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for d in digits:
            number = number * 10 + d

        number += 1

        output = []
        while number != 0:
            output.append(number % 10)
            number = number // 10

        return output[::-1]

        