class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        a=[]
        m=10**9+7
        for i in range(0,len(nums),2):
            x,y=str(nums[i]),str(nums[i+1])
            a.append(int(x+y))
            m=min(int(x+y),m)
        return m