class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        missing = []
        n = len(nums)
        nums = set(nums)
        for i in range(1,n+1):
            if i not in nums:
                missing.append(i)
        return missing