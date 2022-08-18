class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    if (nums.empty())
            return 0;
        
        int last = 0;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[last]) {
                ++last;
                nums[last] = nums[i];//if element is unique gets shifted to initial part of array
            }
        }

        nums.resize(last+1);//modifies the size of array based on provided index
        return nums.size();
    }
};