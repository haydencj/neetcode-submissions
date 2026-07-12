class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for i in range(len(nums) + 1)]
        freq = {}
        res = []

        # fill freq dict
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        print(freq)

        # fill buckets
        for num, count in freq.items():
            buckets[count].append(num)
        
        # iterate through buckets, filling results array
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res