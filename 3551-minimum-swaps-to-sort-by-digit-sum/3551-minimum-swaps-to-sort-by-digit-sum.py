class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        dig={}
        for n in nums :
            tot=0
            t=n
            while t>0:
                tot+=t%10
                t//=10
            dig[n]=tot
        sn=[]
        for i in nums:
            sn.append((dig[i],i))
        sn.sort()
        xx=[]
        for i in sn:
            xx.append(i[1])
        si={}
        for i in range(len(nums)):
            si[nums[i]]=i
        swap=0
        for i in range(len(nums)):
            if nums[i]!=xx[i]:
                swap+=1
            j=si[xx[i]]
            si[nums[i]]=j
            si[nums[j]]=i
            nums[i],nums[j]=nums[j],nums[i]
        return swap