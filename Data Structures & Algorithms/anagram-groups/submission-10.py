class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap with list as values, we store same anagrams here. 
        # the key will be our alphabet array count
        anagrams = defaultdict(list)

        for s in strs:
            # each word will have its own alphabet count
            count = [0] * 26 
            for c in s:
                # increment by 1 for each letter seen in alphabet
                count[ord(c) - ord('a')] += 1
            # store in hashmap, typecast to tuple for hashability
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())