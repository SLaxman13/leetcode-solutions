class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        out = []
        for num in candies:
            if num+extraCandies >= maxi:
                out.append(True)
            else:
                out.append(False)
        return out