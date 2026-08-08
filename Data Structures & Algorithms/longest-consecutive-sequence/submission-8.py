class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # idea: if n - 1 does not exist. n is start of sequence
        longest = 0
        numSet = set(nums)

        for n in numSet:
            # start of seq
            if (n - 1) not in numSet:
                # start seq
                length = 1
                while (n + length) in numSet:
                    length += 1
                # check if longest we've seen
                longest = max(longest, length)
        
        return longest