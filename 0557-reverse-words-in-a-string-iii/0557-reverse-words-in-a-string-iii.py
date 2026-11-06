class Solution:
    def reverseWords(self, s: str) -> str:
        lis = []
        f = s.split()
        for i in f:
            lis.append(i[::-1])
        return " ".join(lis)