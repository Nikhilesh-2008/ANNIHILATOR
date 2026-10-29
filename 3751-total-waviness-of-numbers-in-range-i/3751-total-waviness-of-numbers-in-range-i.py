class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        c=0
        for i in range(num1,num2+1):
            s=str(i)
            for i in range(1,len(s)-1):
                if s[i]>s[i-1] and s[i]>s[i+1]:
                    c+=1
                elif s[i]<s[i-1] and s[i]<s[i+1]:
                    c+=1
        return c