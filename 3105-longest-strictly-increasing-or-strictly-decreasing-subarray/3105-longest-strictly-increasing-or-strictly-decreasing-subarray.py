class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        co=[1]
        c=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c=1
                for j in range(i,len(nums)-1):
                    if nums[j]<nums[j+1]:
                        c+=1
                    else:
                        break
                co.append(c)
            elif nums[i]>nums[i+1]:
                c=1
                for j in range(i,len(nums)-1):
                    if nums[j]>nums[j+1]:
                        c+=1
                    else:
                        break
                co.append(c)
        return max(co)