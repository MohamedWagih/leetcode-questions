class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cities_importance = [0] * n
        
        # we calculate city importance by how many roads it connects
        for c1, c2 in roads:
            cities_importance[c1] += 1
            cities_importance[c2] += 1
        
        # sort cities by importantce 
        # then assing increasing wights starting from the smallest importance
        cities_importance.sort()
        for i in range(len(cities_importance)):
            cities_importance[i] = cities_importance[i] * (i+1)

        return sum(cities_importance)

