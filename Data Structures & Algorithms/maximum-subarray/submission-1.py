class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub

# I used Kadane's Algorithm, which is a Dynamic Programming/Greedy approach. At each element, I decide whether it's better to extend the current subarray or start a new subarray from the current element. I keep track of the maximum subarray sum ending at the current index and the overall maximum seen so far.