class Solution:
    def frequencySort(self, s: str) -> str:
      seen ={}
      for ch in s:
        if ch in seen:
            seen[ch]+=1
        else:
            seen[ch]=1
      so = sorted(seen.items(),key=lambda x:x[1],reverse= True)
      res = ""
      for ch,count in so:
        res+=ch*count
      return res
        