class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: 
            return 0
        
        dp = []
        ans = 0
        min_price = prices[0]
        dp.append(0)


        for i in range(1, len(prices)):
            if (prices[i] < min_price):
                min_price = prices[i]
                dp.append(dp[i-1])
            else:
                dp.append(max(dp[i-1], prices[i] - min_price))
            ans = max(dp[i], ans)
        
        return ans;
        
        