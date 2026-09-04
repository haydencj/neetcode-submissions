class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we found anagrams previously by making a hashmap that counts occurances of each letter in string FOR EACH string
        # then we compare the two hashmaps, if theyre equal then its anagram!

        # how would we do it for > 2 strings? we can use an array the size of the alphabet, each position in the array
        # equates to a letter in the alphabet, we will increment the letter position by one for each we see. 

        # then we use this count array (convert to tuple so its hashable) as a key in a hashmap, the value will be strings with
        # equivalent count tuples

        anagrams = defaultdict(list)

        for s in strs:
            # each string gets its own count
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())