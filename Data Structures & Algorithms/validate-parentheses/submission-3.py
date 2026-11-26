class Solution:
    def isValid(self, s: str) -> bool:
        map = {']': '[', '}': '{', ')': '('}
        stack = []
        for bracket in s:
            if bracket in map.values():
                stack.append(bracket)
            else:
                if len(stack) != 0 and map[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
            
            

            
                
        