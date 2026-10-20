class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans  = []
        for num in range(left,right+1):
            ori = num
            while num>0:
                n = num%10
                if n==0 or ori%n!=0:
                    break
                num = num//10
            if num==0:
                ans.append(ori)
        return ans
