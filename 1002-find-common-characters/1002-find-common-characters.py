class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        res=[]
        for i in set(words[0]):
            c=101
            for j in words:
                c=min(c,j.count(i))
            for k in range(c):
                res.append(i)
        return res