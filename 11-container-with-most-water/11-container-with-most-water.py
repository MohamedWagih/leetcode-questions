class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxArea = 0
        left, right = 0, n-1
        while left < right:
            currArea = (right - left) * (min(height[left], height[right]))
            maxArea = max(currArea, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea