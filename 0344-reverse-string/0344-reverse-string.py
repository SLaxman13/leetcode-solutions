class Solution:
    def reverseString(self, s: list[str]) -> None:
        temp = s.copy()
        for i in range(len(s)):
            s[len(temp)-1-i] = temp[i]

        