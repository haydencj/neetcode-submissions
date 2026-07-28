class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if n - 1 is in nums. if not then n is start of sequence

        # keep track of longest we've seen 
        longest = 0

        # make a set to rid of dupes
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                # start of sequence
                length = 1
                # increase length while num + length exists
                while (num + length) in numSet:
                    length += 1
                # end of seq, compare w longest
                longest = max(longest, length)
        
        return longest