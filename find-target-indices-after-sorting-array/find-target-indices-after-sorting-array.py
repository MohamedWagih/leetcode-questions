class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def merge(left, right):
            res = []
            while left and right:
                if left[0] < right[0]:
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
            mid = len(arr) // 2
            
            left = merge_sort(arr[:mid])
            right= merge_sort(arr[mid:])
            
            return merge(left, right)
        
        def binary_Search(arr, target):
            low = 0
            high = len(arr) - 1
            res = -1
            while low <= high:
                mid = low + (high - low) // 2 
                
                if arr[mid] == target:
                    res = mid
                    high = mid-1
                
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return res
        
        nums = merge_sort(nums)
        out = []
        idx = binary_Search(nums, target)
        if idx == -1:
            return []
        out.append(idx)
        while idx+1 < len(nums) and nums[idx+1] == target:
            idx += 1
            out.append(idx)

        return out        