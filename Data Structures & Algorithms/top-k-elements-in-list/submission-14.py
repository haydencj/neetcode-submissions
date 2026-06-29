class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. make count dict
        count = {n: nums.count(n) for n in nums}
        print(count)
        
        # 2. make freq array
        freq = [[] for i in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        print(freq)

        # 3. make result array
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result