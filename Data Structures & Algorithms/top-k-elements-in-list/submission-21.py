class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        res = []

        # we use idx of bucket to count freq so we need len(nums) + 1 number of buckets
        buckets = [[] for i in range(len(nums) + 1)]
        
        # get frequency of each num
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        print(freq)

        # fill buckets. remember idx = # of occurrences
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        print(buckets)

        # go backwards through buckets, since last bucket would be most freq
        for i in range(len(buckets) - 1, -1, -1): # start, stop, step
            for num in buckets[i]:
                res.append(num)
                # if we've found top k, return
                if len(res) == k:
                    return res