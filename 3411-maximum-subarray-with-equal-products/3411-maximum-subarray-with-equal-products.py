class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        for i in range(n):
            p=1
            gc=0
            lc=1
            le=0
            for j in range(i,n):
                p*=nums[j]
                gc=gcd(gc,nums[j])
                lc=lcm(lc,nums[j])
                le+=1
                if p==lc*gc:
                    l=max(le,l)
        return l