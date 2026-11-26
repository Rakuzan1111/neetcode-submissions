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
                
                stack.append(int(operators[element](int(second), int(first))))
                
            else:
                stack.append(element)
        return int(stack[0])
