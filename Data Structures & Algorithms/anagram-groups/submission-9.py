class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for string in strs: 
            sortedS = ''.join(sorted(string))
            hashMap[sortedS].append(string)

        return list(hashMap.values())