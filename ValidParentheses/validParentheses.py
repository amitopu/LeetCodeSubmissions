class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = '({['
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (top == '(' and i != ')') or (top == '[' and i != ']') or (top == '{' and i != '}'):
                    return False
                
        return len(stack) == 0
        