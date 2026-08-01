class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookUp = set()

        for i in nums:
            if i in lookUp:
                return True
            
            lookUp.add(i)    
        return False        

        