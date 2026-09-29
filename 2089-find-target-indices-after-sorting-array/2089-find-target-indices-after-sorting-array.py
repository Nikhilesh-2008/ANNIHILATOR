class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        rexx=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                rexx.append(i)
        return rexx