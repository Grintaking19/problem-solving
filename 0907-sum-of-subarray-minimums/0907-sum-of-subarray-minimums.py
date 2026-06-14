class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        left = [-1] * n
        right = [n] * n
        stack = []
        # previous less element (left)
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []

        # next less element (right), Non-Strictly for handling duplicates
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        stack = []
        ans = 0
        for i in range(n):
            count = (i-left[i]) * (right[i]-i)
            ans = (ans +  (arr[i] * count)) % MOD

        return ans