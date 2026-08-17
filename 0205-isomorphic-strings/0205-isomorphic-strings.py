class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        use = set()
        for i in range(len(s)):
            if s[i] in map:
                if map[s[i]]!= t[i]:
                    return False
            else:
                if t[i] in use:
                    return False
                map[s[i]]=t[i]
                use.add(t[i])
        return True
        