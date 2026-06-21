class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
            Check permutations inside both of the strings
            Sliding Window approach
            Two individual hashmaps and compare them together
            If the current window is longer than s1, we can shrink the window 
        """

        s1HashMap = defaultdict(int)
        s2HashMap = defaultdict(int)

        for right in range(len(s1)):
            s1HashMap[s1[right]] += 1

        left = 0

        for right in range(len(s2)):
            s2HashMap[s2[right]] += 1

            while (right - left + 1) > len(s1):
                #This means that the window is too large and needs to be shrink 
                s2HashMap[s2[left]] -= 1
                if s2HashMap[s2[left]] == 0: 
                    del s2HashMap[s2[left]]

                left += 1
            
            if s1HashMap == s2HashMap: 
                return True

        return False