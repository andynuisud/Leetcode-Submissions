class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
            Solution: 
            We are given a string S, and want to find the longest substring without duplicate chars

            Sliding Window Problem 
            - Create a HashSet to store the current window
            - Keep a counter of the largest size of the window 

            - Expand the window 
            - max(windowSize, currentSize)

            - Go until the end
        """
        
        hashSet = []

        left = 0
        windowSize = 0

        for right in range(len(s)):
    
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left +=1
            
            hashSet.append(s[right])

            windowSize = max(windowSize, (right - left + 1))

        return windowSize