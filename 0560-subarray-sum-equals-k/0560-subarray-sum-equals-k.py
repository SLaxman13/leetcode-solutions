class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count={0:1}
        curr = 0
        ans = 0
        for num in nums:
            curr = curr+num
            if curr-k in count:
                ans = ans+count[curr-k]
            if curr in count:
                count[curr] = count[curr]+1
            else:
                count[curr]=1
        return ans

        