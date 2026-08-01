class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currentSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):

            # Continue previous subarray OR start a new one
            currentSum = max(nums[i], currentSum + nums[i])

            # Remember the best answer seen so far
            maxSum = max(maxSum, currentSum)

        return maxSum

# I used Kadane's Algorithm, which is a Dynamic Programming/Greedy approach. At each element, I decide whether it's better to extend the current subarray or start a new subarray from the current element. I keep track of the maximum subarray sum ending at the current index and the overall maximum seen so far.