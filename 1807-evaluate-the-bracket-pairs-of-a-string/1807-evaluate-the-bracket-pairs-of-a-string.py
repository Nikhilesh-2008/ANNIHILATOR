class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}
        for i in knowledge:
            d[i[0]]=i[1]
        r=""
        i=0
        while i<len(s):
            if s[i]=='(':
                j=i+1
                while s[j]!=')':
                    j+=1
                qt=s[i+1:j]
                if qt in d:
                    r+=d[qt]
                else:
                    r+='?'
                i=j+1
            else:
                r+=s[i]
                i+=1
        return r