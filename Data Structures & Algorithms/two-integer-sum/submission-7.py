class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create a hashmap of each num index
        idx = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            # find difference required to meet target
            diff = target - nums[i] 

            # if difference is in nums, and it's not the same number at i, return answer.
            if diff in nums and idx[diff] != i: 
                return [i, idx[diff]]