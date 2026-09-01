class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        cumax = nums[0]
        cumin = nums[0]
        for num in nums[1:]:
            if num<0:
                cumax,cumin = cumin,cumax
            cumax = max(num,cumax*num)
            cumin = min(num,cumin*num)
            maxi = max(maxi,cumax)
        return maxi
        