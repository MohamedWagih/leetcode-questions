def merge(left, right):
    output = []
    while left and right:
        if left[0] < right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    
    while left:
        output.append(left.pop(0))
    while right:
        output.append(right.pop(0))
    
    return output
            
    
def merge_sort(l):
    if len(l) == 1:
        return l
    
    left = merge_sort(l[:len(l)//2])
    right = merge_sort(l[len(l)//2:])
    
    return merge(left, right)
        
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)