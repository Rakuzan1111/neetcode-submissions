class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+": lambda a, b: a + b, 
                     "-": lambda a, b: a - b,
                     "/": lambda a, b: a / b,
                     "*": lambda a, b: a * b}
        stack = []
        for element in tokens:
            if element in operators:
                first = stack.pop()
                second = stack.pop()
                
                stack.append(int(operators[element](second, first)))
                
            else:
                stack.append(int(element))
        return stack[0]
