class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        n = len(operations)
        i = 0
        for ops in operations:
            if ops=='D':
                stack.append(int(stack[-1])*2)
            elif ops=='C':
                del stack[-1]
            elif ops=='+':
                a,b = stack[-1],stack[-2]
                stack.append(int(a)+int(b))
            else:
                stack.append(int(ops))
        return sum(stack)