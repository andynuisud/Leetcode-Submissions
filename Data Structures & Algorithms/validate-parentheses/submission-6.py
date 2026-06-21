class Solution:
    def isValid(self, s: str) -> bool:
        
        hashMap = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for i in range(len(s)):

            if s[i] in hashMap: 
                if not stack or stack[-1] != hashMap[s[i]]:
                    return False
                stack.pop()
            else: 
                stack.append(s[i])

        if stack: 
            return False
        return True 