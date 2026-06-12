class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0
        i = 0
        ls = 1 
        nums.sort()
        while i < len(nums):
            cs = 1 
            while i+1 < len(nums):
                if  nums[i] +1 == nums[i+1]:
                    cs +=1
                elif nums[i] != nums[i+1]:
                    break
                if cs > ls:
                    ls = cs
                i+=1
            i+=1

        return ls