class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        n = len(isConnected)
        
        def visit(city):
            isConnected[city][city] = 2
            for adj in range(n):
                if isConnected[city][adj] == 1 and isConnected[adj][adj] == 1:
                    visit(adj)
            
            
        for city in range(n):
            if isConnected[city][city] == 1:
                provinces += 1
                visit(city)
        
        return provinces