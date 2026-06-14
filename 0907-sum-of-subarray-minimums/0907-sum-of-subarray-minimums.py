class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        MOD = 10**9 + 7
        
        stack = []
        res = 0
        arr = [0] + arr + [0]
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                cur = stack.pop()
                res += arr[cur] * (i-cur) * (cur -stack[-1] )
            stack.append(i)
        return res % MOD