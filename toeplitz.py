class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        lastSum = sum(matrix[0])
        for idx, row in enumerate(matrix[1:],start = 1):
            currentSum = sum(row)
            if currentSum != lastSum - matrix[idx-1][-1] + row[0]:
                return False
            else:
                lastSum = currentSum
        return True