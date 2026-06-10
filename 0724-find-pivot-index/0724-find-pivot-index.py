class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum, leftSum = 0,0
        for num in nums:
            totalSum += num
        
        for i in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        return -1