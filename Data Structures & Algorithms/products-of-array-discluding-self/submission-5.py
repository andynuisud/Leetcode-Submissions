class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        current = []
        second = []

        productVal = 1

        # We find everything from the left of I 

        for i in nums: 
            current.append(productVal)
            productVal *= i 

        # Now we find everything from the right of I 

        productVal = 1

        for i in range(len(nums)-1, -1, -1):
            second.append(productVal)
            productVal *= nums[i]

        final = []

        second.reverse()

        for i in range(len(nums)):
            final.append((current[i] * second[i]))

        return final