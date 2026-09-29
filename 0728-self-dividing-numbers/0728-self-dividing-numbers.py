class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            t=i
            f=0
            while t>0:
                dig=t%10
                if dig==0 or i%dig!=0:
                    f=1
                    break
                t//=10
            if f!=1:
                res.append(i)
        return res