class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)
        while small!=0:
            rem = large%small
            large = small
            small = rem
        return large