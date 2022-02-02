class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda interval: interval[0])
        
        curr_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= curr_interval[1]:
                curr_interval[1] = max(curr_interval[1], intervals[i][1])
            else:
                merged.append(curr_interval)
                curr_interval = intervals[i]
        
        merged.append(curr_interval)
        return merged