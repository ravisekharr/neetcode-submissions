class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i==')' and len(stack)>0:
                last=stack.pop()
                if last!='(':
                    return False
            elif i=='}' and len(stack)>0:
                last=stack.pop()
                if last!='{':
                    return False
            elif i==']' and len(stack)>0:
                last=stack.pop()
                if last!='[':
                    return False
            else:
                stack.append(i)
        if len(stack)!=0:
            return False
        return True