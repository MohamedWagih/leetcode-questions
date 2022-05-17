class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices=[]
        indegree={i:0 for i in range(n)}
        for start, end in edges:
            indegree[end] += 1
        
        for vertix in indegree:
            if indegree[vertix] ==0:
                vertices.append(vertix)
        
        return vertices