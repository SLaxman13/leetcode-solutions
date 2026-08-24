class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vo = ['a','e','i','o','u']
        left = 0
        count = 0
        maxi = 0
        for right in range(len(s)):
            if s[right] in vo:
                count +=1
            if right - left + 1 ==k:
                maxi = max(maxi,count)
                if s[left] in vo:
                    count-=1
                left+=1
        return maxi
            

        