class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        """
            Given array piles with number of bananas per pile
            h = number of hours
            We want to find K = Minimum # of bananas per hour 
        """
        left = 1
        right = max(piles)
        res = right

        while left <= right: 
            mid = left + (right - left) // 2

            totalTime = 0

            for pile in piles: 
                totalTime += math.ceil(pile / mid)

            if totalTime <= h: 
                res = mid 
                right = mid - 1
            else:
                left = mid + 1


        return res
                