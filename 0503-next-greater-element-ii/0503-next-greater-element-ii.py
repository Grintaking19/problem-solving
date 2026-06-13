class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []


        for i  in range(2*len(nums)):
            current_idx = i % len(nums)
            
            while stack and nums[current_idx] > nums[stack[-1]]:
                popped_idx = stack.pop()
                result[popped_idx] = nums[current_idx]
            

            if i < len(nums):
                stack.append(current_idx)
            
            # early exit
            if not stack:
                break
        return result