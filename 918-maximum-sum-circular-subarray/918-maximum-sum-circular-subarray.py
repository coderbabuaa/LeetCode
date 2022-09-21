class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        minEndingHere=maxEndingHere=0
        minimum,maximum=float("inf"),float("-inf")
        #Kadane Algorithm
        for num in nums:
            totalSum+=num
            minEndingHere = min(minEndingHere+num,num)
            maxEndingHere = max(maxEndingHere+num,num)
            minimum = min(minimum,minEndingHere)
            maximum = max(maximum,maxEndingHere)
        return max(maximum,totalSum-minimum) if maximum>=0 else maximum