class Solution:
    def trap(self, height: List[int]) -> int:
        
        globalLeft = []
        globalRight = []

        currentMax = 0 
        for i in height: 
            globalLeft.append(currentMax)
            currentMax = max(currentMax, i)

        currentMax = 0 
        for i in range(len(height)-1, -1, -1):
            globalRight.append(currentMax)
            currentMax = max(currentMax, height[i])

        globalRight.reverse()

        #min(globalLeft[i], globalRight[i]) - height[i] 
        #if ans > 0: res += ans

        res = 0

        for i in range(len(height)):
            ans = min(globalLeft[i], globalRight[i]) - height[i]
            if ans > 0: 
                res += ans

        return res