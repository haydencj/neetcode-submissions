class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # idea: if num - 1 does not exist. num is the start of a seq.

        longest = 0
        numSet = set(nums) # sets have o(1) membership look up

        for n in numSet:
            # start of seq
            if (n - 1) not in numSet:
                length = 1 # init length
                while (n + length) in numSet:
                    length += 1
                # end of seq
                longest = max(longest, length)
        
        return longest