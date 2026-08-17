class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = {}
        for ch in sentence:
            if ch in seen:
                seen[ch] +=1
            else:
                seen[ch] = 1
        if len(seen) ==  26:
            return True
        else:
            return False
        