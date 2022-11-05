from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        inDegree = {i:0 for i in range(numCourses)}
        
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
            inDegree[c2] += 1
        
        
        queue = deque()
        
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)
        
        ordered = []
        while queue:
            course = queue.popleft()
            ordered.append(course)
            
            for adj in graph[course]:
                inDegree[adj] -= 1
                if inDegree[adj] == 0:
                    queue.append(adj)
        
        return len(ordered) == numCourses