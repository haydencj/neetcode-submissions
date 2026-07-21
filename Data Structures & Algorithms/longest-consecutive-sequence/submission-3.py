class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # how do we know if its start of a sequence ? n - 1 does not exist.
        # start counting from there. while n + length exists, continue 

        longest = 0
        # for tracking if num exists, w/o duplicates
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet: # start sequence
                length = 1 # starting length of seq
                while (num + length) in numSet: # while we have a valid seq
                    length += 1
                # end of seq, compare with longest we've seen
                longest = max(longest, length)
        
        return longest