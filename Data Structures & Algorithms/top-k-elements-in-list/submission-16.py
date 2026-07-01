class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # bucket = frequency of num appearing

        # 1. make count hashmap
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)

        # 2. create buckets (2d array)
        # 1 bucket for each possible count
        freq = [[] for i in range(len(nums) + 1)] # 7 buckets so we have indices 0-7

        # fill buckets
        for num, cnt in count.items():
            freq[cnt].append(num)
        print(freq)

        # 3. fill results list 
        # go backwards in freq array (most freq -> less freq), 
        # appending to result until length of result == k
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
