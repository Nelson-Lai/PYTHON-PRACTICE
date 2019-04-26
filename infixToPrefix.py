class Solution:
    def __init__(self):
        pass

    operands = ['*','/','+','-','(',')',' ']

    def search(self, input, operator):
        operatorLoc = []
        for index, char in enumerate(input):
            if char == operator:
                operatorLoc.append(index)
            else:
                return input

    '''
    numberReturner will take something like (32 * 5) and return ['32', '5']
    '''
    def numberReturner(self, input, inputIndex):       #Returns first non-operand values to the left and right of the operand as [left, right]
        inputLen = len(input)
        blankPassed = False
        rightOutput = []
        forwardInput =input[(inputIndex+1):]
        for index, char in enumerate(forwardInput):
            if char in self.operands and blankPassed == False:
                    if forwardInput[index+1] not in self.operands:
                        blankPassed = True
            elif char in self.operands and blankPassed == True:
                break
            elif char not in self.operands:
                rightOutput.append(char)
        right = ''.join(rightOutput)

        blankPassed = False
        leftOutput = []
        reversedInput = (input[::-1])[inputLen - inputIndex + 1:]
        for index, char in enumerate(reversedInput, start = 0):
            if char in self.operands and blankPassed == False:
                if reversedInput[index+1] not in self.operands:
                    blankPassed = True
            elif char in self.operands and blankPassed == True:
                break
            elif char not in self.operands:
                leftOutput.append(char)
        leftOutput = leftOutput[::-1]
        left = ''.join(leftOutput)
        return [left, right]

s = Solution()
s.numberReturner('  32     *   54',9)
