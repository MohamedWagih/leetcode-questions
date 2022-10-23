class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        
        for idx, n in enumerate(arr2):
            order[n] = idx
            
        
        for i in range(0, len(arr1)):
            min_order = i
            
            for j in range(i+1, len(arr1)) :
                if order.get(arr1[j], float('inf')) <= order.get(arr1[min_order], float('inf')):
                    min_order = j
                    
            arr1[i] , arr1[min_order] = arr1[min_order] , arr1[i]
            
        
        last_sorted = 0
        for i in range(len(arr1)):
            if arr1[i] not in order:
                last_sorted = i
                break
        
        if last_sorted == 0:
            return arr1
            
        for i in range(last_sorted, len(arr1)):
            min_idx = i
            for j in range(i+1, len(arr1)) :
                if arr1[j] < arr1[min_idx]:
                    min_idx = j
            arr1[i] , arr1[min_idx] = arr1[min_idx] , arr1[i]
        
        return arr1