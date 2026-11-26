class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[0], 0]]
        result = [0] * len(temperatures)
        
        for i in range(1, len(temperatures)):
            if temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i], i])
            else:
                while len(stack)> 0 and stack[-1][0] < temperatures[i]:
                    result[stack[-1][1]] = i-stack[-1][1]
                    stack.pop()
                stack.append([temperatures[i], i])
        return result
                    
            
                
                
                    



