class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        l, r = 0, 1
        longest = 1
        while r < len(s):
            if len(set(s[l:r+1])) == len(s[l:r+1]):
                r +=1
                longest = max(longest, r-l)
            else:
                l +=1
        return longest