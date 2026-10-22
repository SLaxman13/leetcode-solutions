class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # 1. Create a fast, lightweight checklist (0 means prime, 1 means crossed out)
        is_composite = bytearray(n)
        count = 0
        
        # 2. Loop through every number from 2 up to n-1
        for i in range(2, n):
            # If the number has NOT been crossed out yet, it is a prime!
            if is_composite[i] == 0:
                count +=1
                for multiple in range(i * i, n, i):
                    is_composite[multiple] = 1
                    
        return count
