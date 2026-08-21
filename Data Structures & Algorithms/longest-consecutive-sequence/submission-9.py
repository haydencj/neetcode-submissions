class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # pattern: if num - 1 does not exist, then num is start of seq

        longest = 0
        numSet = set(nums) # when checking membership in set o(1)

        for num in nums:
            if (num - 1) not in numSet:
                # start of seq
                length = 1
                while (num + length) in numSet:
                    # while seq is consecutive, increment length
                    length += 1
                longest = max(longest, length)

        return longest
        