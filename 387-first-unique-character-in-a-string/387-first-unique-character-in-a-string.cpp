class Solution {
public:
    int firstUniqChar(string s) {
        int n=s.length();
        //Store Frequency of all characters
        vector <int> fre(26,0);
        for(int i=0;s[i]!='\0';++i)
            fre[s[i]-'a']+=1;
        //Find Non-Repeating Character
        for(int i=0;s[i]!='\0';++i)
            if(fre[s[i]-'a']==1)
                return i;
        
        return -1;
    }
    
};