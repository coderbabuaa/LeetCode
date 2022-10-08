At every step, we have two choices:
1) Rob the current house
2) Skip the current house

If we decide to rob the current house ie nums[i], we cannot have robbed nums[i-1] ie the previous house, hence our total money would be nums[i] + maximum money robbed till nums[i-2] provided that (i-2) >= 0. 

On the other hand if we decide to skip nums[i], our total money would be maxmimum money robbed till nums[i-1].

Thus, at each step, we can model our Dynamic Programming relation as 
dp[i] = Math.max(nums[i] + dp[i-2], dp[i-1]) where dp[x] represents maximum money robbed upto house x.

(Note : A final optimisation can be made if we notice that in our dp array, we only look back 2 places behind, so we can just choose to maintain 2 variables instead of an array leading to an O(1) space solution, and an O(N) time solution.)
