class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # check a is not duplicate. only check if not first value in nums.
            if i > 0 and a == nums[i - 1]:
                continue
            
            # we've checked previous a's, so start left pointer one idx after current a.
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = a + nums[l] + nums[r]
                # sum is too large? we need to move right pointer
                if sum > 0: r -= 1
                # sum is too small? we need to move left pointer
                elif sum < 0: l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    # move left pointer once
                    l += 1
                    # move left pointer continuously if it matches prev left pointer
                    # AND left < right still
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res

