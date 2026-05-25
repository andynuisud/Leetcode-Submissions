class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        arr = set()

        for i in range(len(nums)):

            if nums[i] in arr: 
                return True 
            else:
                arr.add(nums[i])

        return False