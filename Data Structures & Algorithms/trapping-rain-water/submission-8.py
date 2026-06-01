class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height)-1

        leftMin = rightMax = water = 0 

        while left < right: 

            if height[left] < height[right]: 
                leftMin = max(leftMin, height[left])
                water += leftMin - height[left]
                left += 1
            else: 
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
                right -= 1

        return water