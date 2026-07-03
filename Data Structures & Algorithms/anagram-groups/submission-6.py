class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # initialize a dict with list as values

        for word in strs:
            count = [0] * 26 # 26 letters in alphabet
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            result[tuple(count)].append(word)
            # print(result)
        
        return list(result.values())

