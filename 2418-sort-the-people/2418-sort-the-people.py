class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = {}
        l=[]
        i = 0
        for i in range(len(heights)):
            data[heights[i]] = names[i]
        s = dict(sorted(data.items(),key=lambda item:item[0],reverse=True))
        for value in s.values():
            l.append(value)
        return l


        