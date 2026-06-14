class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        nle = [n] * n
        ple = [-1] * n

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                curr = stack.pop()
                nle[curr] = i
                if stack: 
                    ple[curr] = stack[-1]
            stack.append(i)
        while stack:
            curr = stack.pop()
            if stack:
                ple[curr] = stack[-1]
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i] * (nle[i] - ple[i] - 1 ))

        return ans