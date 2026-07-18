class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs: 
            string += str(len(s)) + "#" + s

        return string


    def decode(self, s: str) -> List[str]:

        3#You2#XD
        i = 0 
        res = []
        while i < len(s):
            j = i 
            
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1 
            word = s[ start : start + length]
            res.append(word)

            i = start + length

        return res