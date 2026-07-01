class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and idx[diff] != i:
                return [i, idx[diff]]