class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in range(len(nums)):
            s=[]
            for j in res:
                xx=j+[nums[i]]
                s.append(xx)
            res+=s
        return res