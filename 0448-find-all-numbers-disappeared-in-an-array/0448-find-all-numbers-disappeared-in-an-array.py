class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        temp = []
        ans = []
        s = set(nums)
        for i in range(1,len(nums)+1):
            temp.append(i)
        for j in temp:
            if j not in s:
                ans.append(j)
        return ans
        