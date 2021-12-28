def flip(arr, k):
    arr[:k] = arr[k-1::-1]
    
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans=[]
        for i in range(length):
            max_idx = 0
            for idx, n in enumerate(arr[:length-i]):
                if n > arr[max_idx]:
                    max_idx = idx
            flip(arr, max_idx+1)
            ans.append(max_idx+1)
            flip(arr, length-i)
            ans.append(length-i)

        return ans
            