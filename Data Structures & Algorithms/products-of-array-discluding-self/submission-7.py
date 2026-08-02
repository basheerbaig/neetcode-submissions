class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*(len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]
        return res  

# here res[i] line is already changed as list of prefixed from previous loop we are creating a list where we multiply all numbers except itself

   