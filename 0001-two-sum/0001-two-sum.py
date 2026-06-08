class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap for complement of target
        num_index_map = {}
        for i, n in enumerate(nums):
            num_index_map[n] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_index_map and i != num_index_map[diff]:
                return [i, num_index_map[diff]]
        return []