class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        min_i=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_i:
                min_i=prices[i]
            elif prices[i]-min_i>profit:
                profit=prices[i]-min_i
        return profit
        