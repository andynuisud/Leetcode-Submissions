class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        Try to figure out the amount of K replacements

        So we want to get the occuring value inside the hashmap. 
        After that we are able to add the values + k 
        If its greater than K, we shrink the window until it works
        """

        hashMap = defaultdict(int)
        left = 0 
        maxLength = 0 

        for right in range(len(s)):
            hashMap[s[right]] += 1

            currentMax = max(hashMap.values()) #o(26) = o(1)

            while ((sum(hashMap.values())) - currentMax > k):
                #Shrink the window until it works 
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0: 
                    del hashMap[s[left]]
                left += 1

            maxLength = max(maxLength, (right - left + 1))


        return maxLength