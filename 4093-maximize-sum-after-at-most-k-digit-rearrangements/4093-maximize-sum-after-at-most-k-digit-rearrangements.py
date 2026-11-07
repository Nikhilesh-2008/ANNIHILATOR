class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        m=[]
        for i in range(len(nums)):
            s=str(nums[i])
            d=list(s)
            d.sort(reverse=True)
            x=int("".join(d))
            m.append(x-nums[i])
        m.sort(reverse=True)
        return sum(nums)+sum(m[:k])