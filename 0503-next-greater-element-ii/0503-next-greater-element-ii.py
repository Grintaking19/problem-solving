class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []

        for i  in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                popped_item = stack.pop()
                result[popped_item[1]] = nums[i]
            stack.append((nums[i],i))

        while stack:
            popped = stack.pop()
            for i in range(popped[1]):
                if nums[i] > popped[0]:
                    result[popped[1]] = nums[i]
                    break
        return result