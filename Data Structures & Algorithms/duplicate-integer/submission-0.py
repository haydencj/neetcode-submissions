class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        count = {}

        for n in nums: 
            if n in count:
                return True
            count[n] = count.get(n, 0) + 1

        return False