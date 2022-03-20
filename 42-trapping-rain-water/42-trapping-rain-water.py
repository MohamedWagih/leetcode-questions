class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        leftMax, rightMax = 0, 0
        result = 0
        while left<right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            
            if height[right] > height[left]:
                result += leftMax - height[left]
                left += 1
            else:
                result += rightMax - height[right]
                right -= 1
                
        return result
                        