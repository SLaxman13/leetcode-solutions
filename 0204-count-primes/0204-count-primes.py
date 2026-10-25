class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_composite = bytearray(n)
        count = 0
        for i in range(2, n):
            if is_composite[i] == 0:
                count +=1
                for multiple in range(i * i, n, i):
                    is_composite[multiple] = 1       
        return count
