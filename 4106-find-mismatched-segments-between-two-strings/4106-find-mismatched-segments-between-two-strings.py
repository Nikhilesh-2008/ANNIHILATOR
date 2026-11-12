class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res=[]
        i=0
        while i<len(s1):
            if s1[i]!=s2[i]:
                x=""
                y=""
                j=i
                while i<len(s1) and s1[i]!=s2[i]:
                    x+=s1[i]
                    y+=s2[i]
                    i+=1
                res.append([x,y])
            else:
                i+=1
        return res