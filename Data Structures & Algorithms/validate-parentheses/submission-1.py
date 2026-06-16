class Solution:
    def isValid(self, s: str) -> bool:
        
        #Push the opening bracket onto the stack
        #For every closing bracket, check if the stack is nonempty
        #If the stack is empty it would be valid

        stack = []

        hashMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for character in s: 
            if character in hashMap: 
                if not stack or stack[-1] != hashMap[character]:
                    return False
                stack.pop()
            else:
                stack.append(character)

        if stack: 
            return False
        return True