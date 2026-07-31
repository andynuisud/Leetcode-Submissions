class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}

        for src, dst in prerequisites: 
            if src not in adjList: 
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)

        inProgress, complete = set(), set()

        def dfs(node):
            if node in complete: 
                return True

            if node in inProgress: 
                return False #That means there is a cycle

            inProgress.add(node)

            for neighbor in adjList.get(node, []):
                if not dfs(neighbor):
                    return False 

            inProgress.remove(node)
            complete.add(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True 