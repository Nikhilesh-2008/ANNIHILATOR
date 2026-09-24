class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res=0,i=0;
        vector<int> freq(128,0);
        for(int j=0;j<s.size();j++){
            while(freq[s[j]]>0){
                freq[s[i]]--;
                i++;
            }
            freq[s[j]]++;
            res=max(res,j-i+1);
        }
        return res;
        }
};