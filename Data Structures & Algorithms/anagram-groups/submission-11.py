class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a 'count' tuple as key in dictionary
        # count is 26 elements starting at 0, each index representing
        # a character in the alphabet. increment when char is seen

        res = []
        # key: count, value: list of words w same count
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                # unicode of char - unicode of 'a' gives us location in alphabet
                count[ord(c) - ord('a')] += 1
            # filled out count, store in dict
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())