class Solution {
public:
    int numberOfSubstrings(string s) {
        int ans=0;
        vector<int> f(3,-1);
        for(int i=0;i<s.size();i++){
            int xx=s[i]-'a';
            f[xx]=i;
            if((f[0]!=-1) && (f[1]!=-1) && (f[2]!=-1)){
                ans+=min({f[0],f[1],f[2]})+1;
            }
        }
        return ans;
    }
};