class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        l, r = 0, 1
        longest = 1
        sub = set(s[l])
        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                r +=1
                longest = max(longest, r-l)
            else:
                sub.remove(s[l])
                l +=1
        return longest