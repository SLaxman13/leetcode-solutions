class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = [nums[0]]
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
            l.append(nums[i])
        return l
        