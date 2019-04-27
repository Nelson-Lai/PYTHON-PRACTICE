class Solution:
    def sortArray(self, nums):
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                L = nums[:mid]
                R = nums[mid:]

                mergeSort(L)
                mergeSort(R)

                i = j = k = 0

                # Copy data to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        nums[k] = L[i]
                        i+=1
                    else:
                        nums[k] = R[j]
                        j+=1
                    k+=1
                
                # Checking if any element was left
                while i < len(L): 
                    nums[k] = L[i]
                    i+=1
                    k+=1

                while j < len(R):
                    nums[k] = R[j]
                    j+=1
                    k+=1

                # while max([len(leftArray),len(rightArray)]) > 0:
                #     if len(leftArray) == 0:
                #         outputList.append(num for num in rightArray)
                #     if len(rightArray) == 0:
                #         outputList.append(num for num in leftArray)
                #     else:
                #         a = leftArray[0]
                #         b = rightArray[0]
                #         if a > b:
                #             outputList.append(leftArray.pop(0))
                #         else:
                #             outputList.append(rightArray.pop(0))
        mergeSort(nums)

test = Solution()
nums = [1,2,3,0,4,5,6,7,8]
test.sortArray(nums)
print(nums)