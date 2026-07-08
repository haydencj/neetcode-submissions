class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        # one bucket = frequency 
        # # of buckets = len(nums) + 1 since we use idx value as frequency

        # make count hashamp
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        print(count)

        # initialize buckets
        freq = [[] for i in range(len(nums) + 1)]

        # fill buckets
        # go through each num, cnt in hashmap. assign it to a bucket like freq[cnt] = num
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result = []

        for i in range(len(freq) - 1, -1, -1): #start from last idx, go to 0, in reverse
            for num in freq[i]: # for each value in the bucket
                result.append(num)
                if len(result) == k: # if we have top k then return
                    return result