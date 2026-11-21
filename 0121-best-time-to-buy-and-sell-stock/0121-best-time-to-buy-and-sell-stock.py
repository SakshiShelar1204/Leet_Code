class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minSofar = prices[0]
        res = 0
        for i in range(1, len(prices)):
            minSofar = min(minSofar, prices[i])
            res = max(res, prices[i]-minSofar)
        return res