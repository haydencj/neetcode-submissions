class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # build count hashmap
        # count = { num : nums.count(num) for num in nums }
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1 # get whats at count[num] add one, if nothing there use 0
        
        print(count)

        # build freq array (bucket sort array)
        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        print(freq)

        # build results array
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res