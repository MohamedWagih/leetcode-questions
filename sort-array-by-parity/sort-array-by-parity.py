class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            res = []
            while left and right:
                if left[0] % 2 == 0:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
                    
            while left:
                res.append(left.pop(0))
            while right:
                res.append(right.pop(0))
            
            return res
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            
            left = merge_sort(arr[:len(arr)//2])
            right = merge_sort(arr[len(arr)//2:])
            
            return merge(left, right)
        
        return merge_sort(nums)