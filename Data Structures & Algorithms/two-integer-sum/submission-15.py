class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {nums[i]: i for i in range(len(nums))}
        print(indices)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums and indices[diff] != i:
                return [i, indices[diff]]
