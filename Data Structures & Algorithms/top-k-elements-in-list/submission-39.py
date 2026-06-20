class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = defaultdict(int)

        for i in range(len(nums)):
            hashMap[nums[i]] += 1

        #Use a bucket sort to store all of the information 
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key, value in hashMap.items():
            bucket[value].append(key)

        res = []

        for i in range(len(bucket)-1, -1, -1): 
            for j in bucket[i]:
                res.append(j)
                if len(res) == k: 
                    return res 

        return res