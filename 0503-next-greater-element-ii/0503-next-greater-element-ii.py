class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)):
            l=-1
            for j in range(1,len(nums)):
                ij=(i+j)%len(nums)
                if nums[ij]>nums[i]:
                    l=nums[ij]
                    break
            res.append(l)
        return res