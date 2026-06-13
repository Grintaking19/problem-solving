class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def add(val1, val2):
            return int(val1)+ int(val2)
        def multiply(val1, val2):
            return int(val1) * int(val2)
        def subract(val1, val2):
            return int(val1) - int(val2)
        def divide(val1, val2):
            return int(int(val1)/int(val2))
        operators = {
            '+': add,
            '-': subract,
            '*': multiply,
            '/': divide
        }

        for i in range(len(tokens)):           
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else: 
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(operators[tokens[i]](val1, val2))
        return int(stack[-1])