from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for item in strs:
            profile = [0]*26
            for c in item:
                profile[ord(c) - 97] += 1
            store[tuple(profile)].append(item)
        return [value for value in store.values()]