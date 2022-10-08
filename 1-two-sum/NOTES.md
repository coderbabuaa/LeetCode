# Solution

## Naive approach

We choose an *element* of the *array* and loop through the rest to see if the sum of the *first element* with the *second element* is equal to the *target*. Which, unfortunately, results in time complexity of `O(n²)`.

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    response = []
	for i in range(len(nums)):
		for j in range(i, len(nums)):
			if nums[i] + nums[j] == target:
				response.append([nums[i], nums[j]])
	return response

```

## Efficient approach

In this approach, if we find an *element* that is less than the *target*, we can save the *index* and the *element* in a *hashmap*. Then, if the result of `target - element` already exists in the *map* we know that `target = current-element + the repeated value`. Finding the solution in `O(n)`.

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        
        if remaining in seen:
            return [i, seen[remaining]]
        seen[value] = i 
```


## Sources and more explanation:
[How to solve the two-sum problem - Educative.io](https://www.educative.io/answers/how-to-solve-the-two-sum-problem)  
[How to Solve the Two-Sum Problem | Built In](https://builtin.com/job-interviews/solve-two-sum-problem)  
[Two Ways to Solve the Two Sum Problem | by Saul Feliz](https://medium.com/swlh/two-ways-to-solve-the-two-sum-problem-a158d593eef)  