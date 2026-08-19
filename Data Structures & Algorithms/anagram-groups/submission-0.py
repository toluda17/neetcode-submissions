from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            hashmap[sorted_s].append(s)
        
        for value in hashmap.values():
            result.append(value)

        return result