class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 
        maxProfit = float('-inf')

        for right in range(len(prices)):
            
            if prices[left] > prices[right]:
                left = right

            maxProfit = max(maxProfit, (prices[right] - prices[left]))

        return maxProfit