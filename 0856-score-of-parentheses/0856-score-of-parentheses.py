class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ss=0
        d=0
        for i in range(len(s)):
            xx=s[i]
            if xx=='(':
                d+=1
            else:
                d-=1
                if s[i-1]=='(':
                    ss+=2**d
        return ss