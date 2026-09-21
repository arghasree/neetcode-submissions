class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        max_profit=0

        for i in range(1, len(prices)):
            # print(profit, max_profit)
            profit+=prices[i]-prices[i-1]

            if profit <0:
                profit=0
            
            if profit>max_profit:
                max_profit=profit

        return max_profit