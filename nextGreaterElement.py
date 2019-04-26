class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for index1, num1 in enumerate(nums1):
            start = False
            for num2 in nums2:
                if num2 == num1:
                    start = True
                if num1 < num2 and start == True:
                    nums1[index1] = num2
                    break
                elif num2 == nums2[-1]:
                    nums1[index1] = -1
        return nums1