import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tSet = set(t)
        letterLocations = collections.defaultdict(lambda: [])
        for index, char in enumerate(s):
            if char in tSet:
                letterLocations[char].append(index)
        print(letterLocations)

test = Solution()
test.minWindow('ADOBECODEBANC','ABC')