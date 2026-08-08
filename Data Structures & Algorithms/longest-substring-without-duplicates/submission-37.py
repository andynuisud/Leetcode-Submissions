class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentSize = 0 
        window = set()

        left = 0 

        for right in range(len(s)):
            
            while s[right] in window: 
                window.remove(s[left])
                left += 1

            window.add(s[right])
            currentSize = max(currentSize, len(window))

        if currentSize: 
            return currentSize
        else:
            return 0