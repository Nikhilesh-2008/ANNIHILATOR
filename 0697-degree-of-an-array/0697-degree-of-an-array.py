class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        f=[0]*(max(nums)+1)
        for i in range(len(nums)):
            f[nums[i]]+=1
        x=max(f)
        m=len(nums)
        for i in range(len(f)):
            if f[i]==x:
                ft=nums.index(i)
                lt=len(nums)-1-nums[::-1].index(i)
                m=min(m,lt-ft+1)
        return m