class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        xxx=[]
        while d!={}:
            for i in sorted(list(d.keys())):
                xxx.append(i)
                d[i]-=1
                if d[i]==0:
                    del d[i]
        return xxx