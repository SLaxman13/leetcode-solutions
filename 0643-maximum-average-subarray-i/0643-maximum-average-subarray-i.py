class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        maxi = []
        sub = 0
        index = 0
        while right < len(nums):
            sub+=nums[right]
            index+=1
            while index == k:
                maxi.append(sub)
                sub-=nums[left]
                left+=1
                index-=1
            right+=1
        return max(maxi)/k
        