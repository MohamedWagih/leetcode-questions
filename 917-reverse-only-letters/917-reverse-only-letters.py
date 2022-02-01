class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        str_arr = list(s)
        left, right = 0, len(str_arr)-1 
        
        while left < right:
            while left<len(str_arr) and left < right and not (ord('a')<= ord(str_arr[left])<=ord('z') or ord('A')<= ord(str_arr[left])<=ord('Z')):
                left += 1
            while right>0 and left < right and not (ord('a')<= ord(str_arr[right])<=ord('z') or ord('A')<= ord(str_arr[right])<=ord('Z')):
                right -= 1
            if left<len(str_arr) and right>0 and left < right:
                str_arr[left], str_arr[right] = str_arr[right], str_arr[left]
            left += 1
            right -= 1
            
        return "".join(str_arr)
                