class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # pattern: bucket # == frequency of num
        buckets = [[] for i in range(len(nums) + 1)]

        # create frequency hashmap
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # fill buckets
        for n, cnt in freq.items():
            buckets[cnt].append(n)

        # iterate through buckets in reverse since last bucket is
        # most frequent, remove from each bucket until res == k
        res = []

        for i in range(len(buckets) - 1, -1, -1): # start, stop, step
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res