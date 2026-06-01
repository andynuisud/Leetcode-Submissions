class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        maxPrice = 0

        for right in range(len(prices)):

            if prices[left] > prices[right]:
                left = right

            difference = prices[right] - prices[left]
            maxPrice = max(maxPrice, difference)

        return maxPrice