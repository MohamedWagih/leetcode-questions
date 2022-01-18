"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_importance = 0
        employees_dict = {emp.id: emp for emp in employees}
        
        def dfs(emp):
            nonlocal total_importance
            for subordinate in emp.subordinates:
                dfs(employees_dict[subordinate])
            total_importance += emp.importance
        
        dfs(employees_dict[id])
        return total_importance