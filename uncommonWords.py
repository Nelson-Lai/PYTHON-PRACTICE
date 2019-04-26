import collections
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        listA = A.split()
        listB = B.split()
        commonWords = collections.defaultdict(lambda: 0)
        outputList = []
        for word in listA:
            commonWords[word] += 1
        for word in listB:
            commonWords[word] += 1
        for word in commonWords:
            if commonWords[word] == 1:
                outputList.append(word)
        return outputList


