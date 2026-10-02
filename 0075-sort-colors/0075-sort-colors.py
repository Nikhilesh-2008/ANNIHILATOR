class Solution:
    def sortColors(self, nums: list[int]) -> None:
        d={0:0,
           1:0,
           2:0
        }
        for i in nums:
            d[i]+=1
        xx=0
        for i in range(3):
            for j in range(d[i]):
                nums[xx]=i
                xx+=1