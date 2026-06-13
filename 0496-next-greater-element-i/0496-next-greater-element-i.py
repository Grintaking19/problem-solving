class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    greater_dict[nums2[i]] = nums2[j]
                    break
        print(greater_dict)
        result = []
        for num in nums1:
            if num in greater_dict:
                result.append(greater_dict[num])
            else: 
                result.append(-1)
        return result
