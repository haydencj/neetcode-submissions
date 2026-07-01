class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use 'seen hashmap
        seen = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = seen.get(num, 0) + 1

        return False


            