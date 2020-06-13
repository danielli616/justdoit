class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: 
            return 0
        
        dp = [0] * len(prices)
        min_price = prices[0]

        for i in range(1, len(prices)):
            if (prices[i] < min_price):
                min_price = prices[i]
                dp[i] = dp[i-1]
            else:
                dp[i] = max(prices[i] - min_price, dp[i-1])

        return dp[-1];

# Another solution to make it more concise
class Solution:
  if not prices:
    return 0

  max_profit = 0
  min_price = prices[0]

  for p in prices:
    if p < min_price:
      min_price = p
    elif p - min_price > max_profit:
      max_profit = p - min_price

  return max_profit


        
        
