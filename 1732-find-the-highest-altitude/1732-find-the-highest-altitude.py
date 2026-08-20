class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        high = 0
        for x in gain:
            current+=x
            high = max(high,current)
        return high
        