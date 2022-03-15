class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = float('inf')
        maxSalary = float('-inf')
        
        total = 0
        for s in salary:
            total += s
            minSalary = min(minSalary, s)
            maxSalary = max(maxSalary, s)
        
        avg = (total-maxSalary-minSalary) / (len(salary)-2)
        return avg