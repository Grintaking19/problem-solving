class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap for complement of target
        num_index_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_index_map :
                return [min(i, num_index_map[diff]), max(i, num_index_map[diff])]
            num_index_map[n] = i
        return []