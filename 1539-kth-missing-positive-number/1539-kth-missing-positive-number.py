class Solution:
    # Cycle Sort Pattern
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        n = len(arr)
        
        while i < n:
            j = arr[i] - 1
            if 0 <= j < n and arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i += 1
                
        extra_nums = set()
        missing = []
        
        for i in range(n):
            if len(missing) < k:
                if arr[i] -1 != i:
                    missing.append(i+1)
                    extra_nums.add(arr[i])
        
        # if we still not completed missing
        candidate = n + 1
        while len(missing) < k:
            if candidate not in extra_nums:
                missing.append(candidate)
            candidate += 1
        
        return missing[-1]
        