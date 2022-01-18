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
        
        def get_emp(id):
            for emp in employees:
                if emp.id == id:
                    return emp
                
        def dfs(emp):
            nonlocal total_importance
            for subordinate in emp.subordinates:
                dfs(get_emp(subordinate))
            total_importance += emp.importance
        
        dfs(get_emp(id))
        return total_importance