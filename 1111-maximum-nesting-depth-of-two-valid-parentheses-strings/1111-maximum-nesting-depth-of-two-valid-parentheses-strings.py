class Solution:
    def maxDepthAfterSplit(self, seq: str):
        ans=[]
        d=0
        for i in seq:
            if i=='(':
                d+=1
                ans.append(d%2)
            else:
                ans.append(d%2)
                d-=1
        return ans