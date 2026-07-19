class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # trick: if num - 1 does not exist, 
        # then num is start of a sequence
        
        # keep track of longest seq we'eve seen.
        longest = 0

        # use set to discard duplicates
        numSet = set(nums)

        for n in nums:
            # if n - 1 doesn't exist, start counting
            if n - 1 not in numSet:
                # start of seq, length is 1
                length = 1
                # each n + length we see, increment length and continue
                while (n + length) in numSet:
                    length += 1
                # seq end, check if longer than longest
                longest = max(longest, length)
        
        return longest
