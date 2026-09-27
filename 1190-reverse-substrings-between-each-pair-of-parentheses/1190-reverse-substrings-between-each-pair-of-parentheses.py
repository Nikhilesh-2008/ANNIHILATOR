class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=list(s)
        res=""
        st=[]
        for i in range(len(l)):
            if l[i]=='(':
                st.append(res)
                res=""
            elif l[i]==')':
                res=res[::-1]
                res=st.pop()+res
            else:
                res+=l[i]    
        return res