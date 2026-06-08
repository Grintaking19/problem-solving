class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash maps using frequency lists Solution
        dictS = defaultdict(list)
        for s in strs:
            countS = [0] *26
            for c in s:
                countS[ord(c) - ord('a')] +=1
            dictS[tuple(countS)].append(s)

        return list(dictS.values())