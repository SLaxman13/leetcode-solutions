class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i!=max(nums):
                ans = max(nums) - i
                count+=ans
        return count

        