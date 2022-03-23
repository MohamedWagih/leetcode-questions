from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
            indegree[c2] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                
        orderedCourses = []
        while queue:
            course = queue.popleft()
            orderedCourses.append(course)
            for adj in graph[course]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
        
        return len(orderedCourses) == numCourses