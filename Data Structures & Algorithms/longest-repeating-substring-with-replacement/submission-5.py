class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashMap = defaultdict(int)
        maxSize = float('-inf')
        left = 0 

        for right in range(len(s)):

            hashMap[s[right]] += 1

            while (right - left + 1 - max(hashMap.values())) > k: 
                hashMap[s[left]] -= 1
                left += 1

            maxSize = max(maxSize, (right - left + 1))

        return maxSize