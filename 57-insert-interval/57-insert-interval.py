class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, start, end = 0, 0, 1
        result = []
        
        while i < len(intervals) and newInterval[start] > intervals[i][end]:
            result.append(intervals[i])
            i += 1
            
        while i < len(intervals) and newInterval[end] >= intervals[i][start] :
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            print(newInterval)
            i += 1
        
        result.append(newInterval)
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
            
        return result