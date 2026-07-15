class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # group anagrams using a hashmap where the key 
        # tells us how many of each letter is in a word

        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26 # each word has a count
            for c in word:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        return list(anagrams.values())
