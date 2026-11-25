class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            ana = "".join(sorted(word))

            if ana not in anagram_map:
                anagram_map.update({ana: []})
            
            
            anagram_map[ana].append(word)
        return list(anagram_map.values())