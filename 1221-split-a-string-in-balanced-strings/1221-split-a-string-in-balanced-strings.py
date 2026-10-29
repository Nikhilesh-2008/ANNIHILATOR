class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=0
        r=0
        c=0
        for i in s:
            if i=='L':
                l+=1
            else:
                r+=1
            if l==r:
                c+=1
                l=r=0
        return c