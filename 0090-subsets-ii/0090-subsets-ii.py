class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        xxx=[[]]
        end=0
        for i in range(len(nums)):
            st=0
            if i>0 and nums[i]==nums[i-1]:
                st=end
            end=len(xxx)
            for j in range(st,end):
                xxx.append(xxx[j]+[nums[i]])
        return xxx