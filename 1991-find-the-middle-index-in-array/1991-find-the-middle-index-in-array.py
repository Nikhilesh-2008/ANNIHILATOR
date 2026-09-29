class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        tot=sum(nums)
        l=0
        for i in range(len(nums)):
            r=tot-l-nums[i]
            if l==r:
                return i
            l+=nums[i]
        return -1