class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumL, sumR = [] , []
        resultL, resultR = 0, 0
        i, j = 0, len(nums)-1
        while i <= len(nums) -1:
            resultL += nums[i]
            sumL.append(resultL)
            i +=1
        while j >= 0:
            resultR +=nums[j]
            sumR.append(resultR)
            j -=1
        print(sumL)
        print(sumR[::-1])
        sumR_rev = sumR[::-1]
        for i in range(len(sumL)):
            if sumL[i] == sumR_rev[i]:
                return i
        return -1