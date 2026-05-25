class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxNumber = 0 
        current = 0 

        for i in range(len(nums)):
            if nums[i] == 0:
                maxNumber = max(current, maxNumber)
                current = 0
            else:
                current += 1

        final = max(current, maxNumber)
        return final
