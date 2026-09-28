class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        n = len(operations)
        i = 0
        for ops in operations:
            if ops=='D':
                stack.append(int(stack[-1])*2)
                res+=int(stack[-1])*2
            elif ops=='C':
                res-=stack.pop()
            elif ops=='+':
                a,b = stack[-1],stack[-2]
                stack.append(int(a)+int(b))
                res+=int(a)+int(b)
            else:
                stack.append(int(ops))
                res += int(ops)
        return sum(stack)