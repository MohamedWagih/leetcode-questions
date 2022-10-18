class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = {}
        freq2 = {}
        
        for n in nums1:
            freq1[n] = freq1.get(n, 0) + 1
            
        for n in nums2:
            freq2[n] = freq2.get(n, 0) + 1
            
        for n in freq1:
            if n in freq2:
                freq1[n] = min(freq1[n], freq2[n])
            else:
                freq1[n] = 0
                
        res = []
        for n, f in freq1.items():
            res += [n] * f
            
        return res
        
        
        