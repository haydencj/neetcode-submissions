class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        # if num - 1 does not exist, then its the start of a sequence

        # get rid of duplicates here
        numSet = set(nums)
        # we will use this value to store the longest seq we've seen
        longest = 0

        for n in nums:
            # if its start of the sequence
            if (n - 1) not in nums:
                # start counting the length
                length = 1
                # while n + 1 exist (valid seq)
                while (n + 1) in numSet:
                    length += 1
                    n += 1
                # check if its longer than what we've seen
                longest = max(length, longest)
        
        return longest