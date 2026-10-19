class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ls =[]
        for i in range(1,n+1):
            if i%3!=0 and i%5!=0:
                ls.append(str(i))
            elif i%3==0 and i%5!=0:
                ls.append("Fizz")
            elif i%5==0 and i%3!=0:
                ls.append("Buzz")
            elif i%3==0 and i%5==0:
                ls.append("FizzBuzz")
        return ls

        