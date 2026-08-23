class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right= 0
        mini = []
        sub = 0
        while right < len(nums):
            sub+=nums[right]
            while sub>=target:
                mini.append(right-left+1)
                sub-=nums[left]
                left+=1
            right+=1
        return 0 if len(mini)==0 else min(mini)
        