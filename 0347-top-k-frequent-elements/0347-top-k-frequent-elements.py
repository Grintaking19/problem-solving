class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict={}
        for i in range(len(nums)): 
            freqDict[nums[i]] = freqDict.get(nums[i], 0) + 1
        res = []
        for num, counter in freqDict.items():
            res.append([counter, num])
        res.sort(reverse=True)
        print(res)
        return [p[1] for p in res][:k]