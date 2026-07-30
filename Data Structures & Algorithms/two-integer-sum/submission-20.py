class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {nums[i]: i for i in range(len(nums))}

        for i, n in enumerate(nums): 
            diff = target - n
            if diff in nums and indices[diff] != i: # ensure diff is not same element as n (by checking idx)
                return [i, indices[diff]]