class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rateBound = max(piles)
        if h == len(piles):
            return rateBound
        l, r = 1, rateBound
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            totalH = 0
            for p in piles:
                totalH += (p-1)//mid + 1
            if totalH <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res