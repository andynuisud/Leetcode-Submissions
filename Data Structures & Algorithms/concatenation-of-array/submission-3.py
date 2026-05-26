class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        i = 0
        curr = 0 

        while i != len(nums) * 2: 

            if i == len(nums):
                curr = 0 

            ans.append(nums[curr])
            curr += 1
            i += 1
        
        return ans 