class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0: # if positive, turn it negative to mark as visited
                nums[temp] *= -1
        missing = []
        for i, n in enumerate(nums):
            if n > 0:
                missing.append(i+1)
        return missing