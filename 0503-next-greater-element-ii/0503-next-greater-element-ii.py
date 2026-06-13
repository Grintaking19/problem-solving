class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # greater_dict = {}
        # stack = [] # Monotonic Decreasing Stack

        # for i in range(len(nums)):
        #     while stack and nums[i] > stack[-1][0]:
        #         popped_item = stack.pop()[0]
        #         greater_dict[popped_item] = nums[i]
        #     stack.append((nums[i], i))

        # while stack:
        #     popped_tuple = stack.pop()
        #     found = False
        #     for i in range(popped_tuple[1]):
        #         if nums[i] > popped_tuple[0]:
        #             greater_dict[popped_tuple[0]] = nums[i]
        #             found = True
        #             break
        #     if found == False:
        #         greater_dict[popped_tuple[0]] = -1
        
        # return [greater_dict[x] for x in nums]


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