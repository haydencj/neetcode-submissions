class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if n - 1 does not exist, then n is start of seq

        longest = 0
        numSet = set(nums) # removes dupes

        for n in numSet:
            if n - 1 not in numSet:
                length = 1 # initialize length to 1
                # keep checking if consecutive
                while (n + length) in numSet:
                    length += 1
                # compare w longest we've seen
                longest = max(longest, length)
        
        return longest

