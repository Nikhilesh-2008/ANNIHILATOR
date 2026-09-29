class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        c=1
        r=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                c=1
            r=max(r,c)
        return r