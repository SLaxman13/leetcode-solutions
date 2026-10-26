class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for ch in s:
            if 'A'<=ch <= 'Z':
                lo = chr(ord(ch)+32)
                res.append(lo)
            else:
                res.append(ch)
        return "".join(res)        