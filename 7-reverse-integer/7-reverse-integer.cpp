class Solution {
public:
    int reverse(int x) {
        bool neg = false;
        if(x < 0){
            neg = true;
            long long tmp = x * -1LL;
            //LL is the suffix for long-long, which is 64-bit
            if(tmp > INT_MAX) return 0;//Maximum value for a variable of type int .
            x = tmp;
        }
        
        int ans = 0;
        
        while(x){
            long long tmp = ans * 10LL + x % 10;
            if(tmp > INT_MAX) return 0;
            ans = tmp;
            x /= 10;//reversing digits using recursion
        }
        
        if(neg){
            ans *= -1;//
        }
        
        return ans;
    }
};