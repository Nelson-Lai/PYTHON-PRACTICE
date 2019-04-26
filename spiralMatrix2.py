class Solution:
    def generateMatrix(self, n):

        def clockwiseFill(startIndex,stopIndex,startNumber):
            if startIndex > stopIndex:
                return
            for idx in range(startIndex,stopIndex):
                outputMatrix[startIndex][idx] = startNumber
                startNumber += 1
            for idx in range(startIndex+1,stopIndex):
                outputMatrix[idx][stopIndex-1] = startNumber
                startNumber += 1
            for idx in range(stopIndex-2,startIndex-1,-1):
                outputMatrix[stopIndex-1][idx] = startNumber
                startNumber += 1
            for idx in range(stopIndex-2,startIndex,-1):
                outputMatrix[idx][startIndex] = startNumber
                startNumber += 1
            clockwiseFill(startIndex+1,stopIndex-1,startNumber)

        size = n
        outputMatrix = [[0 for x in range(size)] for y in range(size)]
        clockwiseFill(0,size,1)
        return outputMatrix

test = Solution()
outputMatrix = test.generateMatrix(5)
print(outputMatrix)