class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=0
        for i in digits:
            s=s*10+i
        s+=1
        r=[]
        for i in str(s):
            r.append(int(i))
        return r