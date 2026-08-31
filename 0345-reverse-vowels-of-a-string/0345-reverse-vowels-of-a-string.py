class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a', 'e','i','o','u','A','E','I','O','U']
        s = list(s)
        i = 0
        j = len(s)-1
        while i<j:
            if s[i] not in vow:
                i+=1
            elif s[j]  not in vow:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)