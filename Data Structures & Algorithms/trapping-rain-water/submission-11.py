class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = [0 for _ in range(len(height))]
        maxRight = [0 for _ in range(len(height))]

        currentLeftMax=0
        currentRightMax=0

        for i in range(1, len(height)):
            currentLeftMax = max(currentLeftMax, height[i-1])
            maxLeft[i] = currentLeftMax

        for i in range(len(height)-2, -1, -1):
            currentRightMax = max(currentRightMax, height[i+1])
            maxRight[i] = currentRightMax

        res = 0

        for i in range(len(maxLeft)):
            ans = (min(maxLeft[i], maxRight[i]) - height[i])
            if ans > 0: 
                res += ans

        return res