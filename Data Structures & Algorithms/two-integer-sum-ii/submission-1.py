class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            t = numbers[l] + numbers[r]
            # if we're over target, move right pointer
            if t > target: r -= 1
            # if we're under target, move left pointer
            elif t < target: l += 1
            # if they equal, return answer
            else: return [l + 1, r + 1]
        