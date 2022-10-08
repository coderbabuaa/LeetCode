pub mod Solution {
    use std::collections::HashMap;

    pub fn two_sum(nums: Vec<usize>, target: usize) -> Vec<usize> {
        let mut memo: HashMap<usize, usize> = HashMap::new();
        let mut result = Vec::new();
        
        for (index, value) in nums.iter().enumerate() {
            let remain = target - nums[index];
            
            if memo.contains_key(&remain) {
                result = vec![index, memo[&remain]];
                break;
            }
            memo.insert(*value, index);
        }
        result
    }
}
