class Solution {
public:
    bool isPalindrome(int x) {
        long int rev,sum=0;
        long int a=x;
        while(x>0){
            rev=x%10;
            sum=(sum*10)+rev;
            x=x/10;
        }
        if (a==sum)
            return true;
        else
            return false;
    }
};