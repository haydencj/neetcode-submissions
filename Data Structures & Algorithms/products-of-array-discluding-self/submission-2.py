class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix * postfix = answer
        # nums = [1,2,4,6]

        # result array will be same size as nums
        result = [0] * len(nums)

        # prefix for first value is always 1
        prefix = 1
        # result after prefix = [1, 1, 2, 8]
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # postfix for last value is always 1
        postfix = 1
        # result after postfix = [48,24,12,8] (answer)
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result