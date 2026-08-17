class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        temp = set()
        for ch in arr:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
        for value in seen.values():
            temp.add(value)
        return len(temp) == len(seen)
