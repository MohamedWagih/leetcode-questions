from heapq import *
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key =lambda course: course[1])
        max_heap = []
        
        time = 0
        for course in courses:
            duration = course[0]
            lastDay = course[1]
            
            if (time+duration) <= lastDay:
                heappush(max_heap, -duration)
                time += duration
            elif max_heap and -max_heap[0] > duration:
                time -= -heappop(max_heap)
                time += duration
                heappush(max_heap, -duration)
        
        return len(max_heap)