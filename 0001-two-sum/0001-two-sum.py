class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sorting + Two Pointer Solution
        num_index_array = []
        for i, num in enumerate(nums):
            num_index_array.append([num, i])
        
        num_index_array.sort()
        
        i, j = 0, len(nums)-1
        while i < j:
            result = num_index_array[i][0] + num_index_array[j][0]
            if result < target:
                i+=1
            elif result > target:
                j-=1
            elif result == target: 
                return [min(num_index_array[i][1], num_index_array[j][1]),
                        max(num_index_array[i][1], num_index_array[j][1])]
        return []