class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        counterS = {}
        for i in range(len(s)):
            counterS[s[i]] =  counterS.get(s[i], 0) + 1
            counterS[t[i]] =  counterS.get(t[i], 0) - 1
        
        for c in list(counterS.values()):
            if c != 0 :
                return False

        return True
        