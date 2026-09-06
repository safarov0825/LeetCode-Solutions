class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        lowest = prices[0]

        for p in prices:
            if p < lowest:
                lowest = p
                pass
                
            if p - lowest > profit:
                profit = p -lowest

        return profit
        