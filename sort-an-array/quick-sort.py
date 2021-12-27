import random
def partition(l, low, high):
    pivot_idx = random.choice(range(low, high+1))
    l[pivot_idx], l[low] = l[low], l[pivot_idx]
    
    pivot = l[low]
    pivot_idx = low
    
    while low < high:
        
        while low < len(l) and l[low] <= pivot:
            low += 1 
        
        while l[high] > pivot:
            high -= 1
            
        if low < high:
            l[low], l[high] = l[high], l[low] 
    
    l[pivot_idx] , l[high] = l[high], l[pivot_idx]
    return high
    
    
def quick_sort(l, low, high):
    if low < high:
        pivot_idx = partition(l, low, high)
        quick_sort(l, low, pivot_idx-1)
        quick_sort(l, pivot_idx+1, high)
        
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums,0, len(nums)-1)
        return nums
