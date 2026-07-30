class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count array for alphabet count

        # value will be list of str w same key (count array)
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s) # typecast to tuple bc list is not hashable (so it cant be a key)

        return list(anagrams.values())