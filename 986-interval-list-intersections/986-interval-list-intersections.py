class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        
        p1, p2 = 0, 0
        start, end = 0, 1
        while p1 < len(firstList) and p2 < len(secondList):
            interval1 = firstList[p1]
            interval2 = secondList[p2]
            intersected = False
            if interval1[start] <= interval2[start]  <= interval1[end] or interval2[start] <= interval1[start]  <= interval2[end]:
                intersected = True
                intersection_start = max(interval1[start], interval2[start])
                intersection_end = min(interval1[end], interval2[end])
                result.append([intersection_start, intersection_end])
            
            if interval1[end] < interval2[end]:
                p1 += 1
            else:
                p2 += 1
                    
        return result
                
            