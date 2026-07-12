class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        anagrams = defaultdict(list) # value will be a list

        # loop through strs
        for word in strs:
            # each word will have its own alphabet count array
            count = [0] * 26
            # loop through word
            for c in word:
                count[ord(c) - ord('a')] += 1
            # save in anagrams dict. typecast to tuple since its hashable
            anagrams[tuple(count)].append(word)

        # return anagrams values as a list
        return list(anagrams.values())
            