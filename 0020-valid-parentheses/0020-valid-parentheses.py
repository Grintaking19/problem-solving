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
            elif len(stack) == 0:
                return False
            elif openToCloseBracket[stack[-1]] == c:
                stack.pop()
            else:
                return False

        if len(stack) != 0:
            return False
            
        return True