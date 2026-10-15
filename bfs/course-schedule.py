class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] *numCourses

        for a, b in prerequisites:
            graph[b].append[a]
            indegree[a]+=1

        q = deque([i for i in range(numCourses) if indegree[i]==0])
        taken = 0

        while q:
            v = q.popleft()
            taken += 1 
            for u in graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    q.append(u)

        return taken == numCourses
