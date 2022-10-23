class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        
        for idx, n in enumerate(arr2):
            order[n] = idx
        
        # max number in input is 1000 so we can shift the elements not in order by 1000 to be sorted after these presented in order
        return sorted(arr1, key=lambda a: order.get(a, 1000 + a) )