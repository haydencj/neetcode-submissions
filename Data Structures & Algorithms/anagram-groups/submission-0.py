from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                # ord('a') is smallest unicode, which is why we subtract it. 
                # it gives us position of letter in alphabet/array
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(word)
        
        return list(result.values())



    