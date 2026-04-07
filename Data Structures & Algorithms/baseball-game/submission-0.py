class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(int(stack[-1] + stack[-2]))
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                doub = stack[-1] * 2
                stack.append(int(doub))
            else:
                stack.append(int(op))
        
        return sum(stack)
            
            