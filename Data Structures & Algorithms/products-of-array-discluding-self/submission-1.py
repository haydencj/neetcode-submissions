class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        # calculate prefix -> store in result
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # calculate postfix -> multiply by prefix value in result
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1): # start from last index, going till 0, in reverse
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
