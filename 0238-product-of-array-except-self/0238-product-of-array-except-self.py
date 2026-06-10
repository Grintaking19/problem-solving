class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultR, resultL = 1, 1
        productL, productR = [], []

        for num in nums:
            resultL *= num
            productL.append(resultL)

        for num in nums[::-1]:
            resultR *= num
            productR.append(resultR) 
        productR = productR[::-1]

        result = []
        for i in range(len(nums)):
            if i == 0: 
                result.append(productR[i+1])
                continue
            if i == len(nums)-1:
                result.append(productL[i-1])
                continue
            result.append(productL[i-1]*productR[i+1])            

        return result

        