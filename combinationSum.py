class Solution:
    def combinationSum4(self, nums, target):

        memo = {0:1}

        def recurseHelper(num):
            if num in memo:
                return memo[num]
            if num < 0:
                return 0

            memo[num] = sum([recurseHelper(num - addition) for addition in nums])
            return memo[num]

        return recurseHelper(target)



test = Solution()
test.combinationSum4([1,2,3],4)