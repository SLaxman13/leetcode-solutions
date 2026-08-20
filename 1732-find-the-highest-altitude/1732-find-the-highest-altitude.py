class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        l=[gain[0]]
        for i in range(1,len(gain)):
            gain[i] = gain[i-1]+gain[i]
            l.append(gain[i])
        return max(l)
        