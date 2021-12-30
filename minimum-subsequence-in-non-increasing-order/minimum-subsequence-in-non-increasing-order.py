class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        sub_sum = 0
        res = []
        for num in nums:
            sub_sum += num
            res.append(num)
            if sub_sum > total_sum-sub_sum:
                return res
        return res