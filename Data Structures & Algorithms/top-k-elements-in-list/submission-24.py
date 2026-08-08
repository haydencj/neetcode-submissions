class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # one bucket per # of num appearances
        # create a freq hashmap to count appears
        # buckets are a 2d array, where index of outer array is freq
        # inner array is nums with that with that freq

        buckets = [[] for i in range(len(nums) + 1)]
        freq = {}

        # create freq map
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # fill buckets
        for n, cnt in freq.items():
            buckets[cnt].append(n)

        # go through buckets backwards since last bucket is most freq
        # append to res array until lenght of res == k
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                # if we found top k return
                if len(res) == k:
                    return res