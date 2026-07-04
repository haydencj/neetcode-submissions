class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # each bucket is the frequency of a number's appearance
        # total buckets is len(nums) + 1, since we have 0 index
        # after our buckets are created we will loop through them backwards
        # b/c the most frequent numbers are at the end. 

        count = {}

        # get count of each num
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)

        # initialize buckets
        freq = [[] for i in range(len(nums) + 1)]

        # fill buckets
        for num, cnt in count.items():
            freq[cnt].append(num)
        print(freq)

        result = []
        # get top k freq elements
        for i in range(len(freq) - 1, 0, -1): # start, stop, step
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result