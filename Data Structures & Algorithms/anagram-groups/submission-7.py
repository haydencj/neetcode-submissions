class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # empty dict where values are lists
        
        for word in strs:
            count = [0] * 26 # 26 letters in alphabet
            for c in word:
                count[ord(c) - ord('a')] += 1
            # after we filled count array assign it in hashmap
            result[tuple(count)].append(word)
        
        return list(result.values())