class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n=nums.size();
        vector<int> indices;
        for(int i=0;i<n;i++){
            int dif=target-nums[i];
            for(int j=i+1;j<n;j++)
            {
                if(nums[j]==dif){
                    indices.push_back(i);
                    indices.push_back(j);
                    return indices;
                }
            }
        }
        return indices;
    }
};