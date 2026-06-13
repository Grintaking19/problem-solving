class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}
        stack = [] # Monotonic Decreasing Stack

        for num in nums2:
            while stack and num > stack[-1]: # Pop and assign dictioanry
                popped_item = stack.pop()
                greater_dict[popped_item] = num

            stack.append(num)

        while stack:
            popped_item = stack.pop()
            greater_dict[popped_item] = -1
        
        return [greater_dict[x] for x in nums1]