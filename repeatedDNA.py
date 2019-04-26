class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        window = s[0:10]
        seenSequences = set()
        seenSequences.add(window)
        outputSet = set()
        for letter in s[10:]:
            window = window[1:] + letter
            if window in seenSequences:
                outputSet.add(window)
            else:
                seenSequences.add(window)
        return list(outputSet)


test = Solution()
test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")