bool isValid(char* s) {
    char q[10000];
    int j=0;
    int n=strlen(s);
    if(n%2!=0)
        return false;
    for(int i=0;i<n;i++){
        if(s[i]=='(' || s[i]=='[' || s[i]=='{')
            q[j++]=s[i];
        else if(s[i]==')'){
            if(j==0 || q[j-1]!='(')
                return false;
            j--;
        }
        else if(s[i]==']'){
            if(j==0 || q[j-1]!='[')
                return false;
            j--;
        }
        else if(s[i]=='}'){
            if(j==0 || q[j-1]!='{')
                return false;
            j--;
        }
    }
    if(j==0)
        return true;
    else
        return false;
}