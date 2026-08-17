class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen = {}
        temp=[]
        for ch in arr:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch]=1
        for key,value in seen.items():
            if key == value:
                temp.append(key)
        if temp:
            return max(temp)
        return -1

        