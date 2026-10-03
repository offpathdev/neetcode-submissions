from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = defaultdict(int)
        for c in s:
            store[c] += 1
        for c in t:
            store[c] -= 1
        return set(store.values()) == {0}