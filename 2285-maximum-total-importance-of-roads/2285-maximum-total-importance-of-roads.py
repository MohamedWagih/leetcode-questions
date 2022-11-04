from collections import defaultdict
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        importance = defaultdict(int)
        
        for c1, c2 in roads:
            importance[c1] += 1
            importance[c2] += 1
            
        cities = sorted(importance.items(), key=lambda k: k[1], reverse=True)
        
        weights= [0] * n
        for city, weight in cities:
            weights[city] = n
            n -= 1

        total_importance = 0
        for c1, c2 in roads:
            total_importance += weights[c1] + weights[c2]

        return total_importance


