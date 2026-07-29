class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        adjList = defaultdict(list)

        if beginWord not in wordList:
            wordList = [beginWord] + wordList

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if sum(a != b for a, b in zip(wordList[i], wordList[j])) == 1: # We want to find the difference of 1
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])

        #Use a BFS 
        length = 1
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append(beginWord)

        while q: 
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return length 

                for neighbor in adjList[curr]:
                    if neighbor not in visited: 
                        visited.add(neighbor)
                        q.append(neighbor)
            length += 1
            
        return 0