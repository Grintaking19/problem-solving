class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToCloseBracket = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }

        for c in s:
            if c in openToCloseBracket:
                stack.append(c) 
            else:
                if stack and openToCloseBracket[stack[-1]] == c:
                    stack.pop()
                else: return False
        
        return True if not stack else False