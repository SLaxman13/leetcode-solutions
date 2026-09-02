class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(map(str,digits)))
        res+=1
        a = list(map(int, str(res)))
        return a