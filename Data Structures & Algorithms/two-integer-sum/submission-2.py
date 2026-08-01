class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        
        # for i in range(len(nums)):
        #     pair = target - nums[i]
        #     for j in range(i+1,len(nums)):
        #         if pair == nums[j]:
        #             return [i,j];
            


        