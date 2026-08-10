class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1
        
        while l < r:
            # compute area
            area = min(heights[l], heights[r]) * (r - l)
            # compare current area with largest we've seen
            res = max(res, area)
            # we move pointer w shortest height
            if heights[l] <= heights[r]: 
                l += 1
            else:
                r -= 1
        return res