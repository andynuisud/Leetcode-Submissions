class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s1Hash = defaultdict(int)
        s2Hash = defaultdict(int)

        for i in range(len(s1)):
            s1Hash[s1[i]] += 1

        left = 0
        
        for right in range(len(s2)):

            s2Hash[s2[right]] += 1

            if (right - left) + 1 > len(s1):
                s2Hash[s2[left]] -= 1

                if s2Hash[s2[left]] == 0:
                    del s2Hash[s2[left]]

                left += 1

            if s1Hash == s2Hash:
                return True 

        return False