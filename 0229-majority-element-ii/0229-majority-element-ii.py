class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen={}
        result=[]
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for key,value in seen.items():
                if value > len(nums)//3:
                    result.append(key)
        return result