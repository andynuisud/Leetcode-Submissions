class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        adjList = defaultdict(list)

        if beginWord not in wordList: 
            wordList = [beginWord] + wordList

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):

                if sum(a != b for a, b in zip(wordList[i], wordList[j])) == 1: 
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])

        length = 1
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)

        while q: 
            for i in range(len(q)):
                current = q.popleft()

                if current == endWord: 
                    return length

                for neighbor in adjList[current]:
                    if neighbor not in visited: 
                        visited.add(neighbor)
                        q.append(neighbor)

            length += 1

        return 0 