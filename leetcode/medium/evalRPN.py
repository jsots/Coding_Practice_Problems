class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            "+" : operator.add, 
            "-": operator.sub, 
            "*": operator.mul, 
            "/": lambda x, y: math.trunc(x / y)
            }
        # What if not acceptible operand?
        # What kind of division?
        # What if divide by 0? Return inf?
        solution_stack = []
        for token in tokens:
            if token in operands:
                b = solution_stack.pop()
                a = solution_stack.pop()
                solution_stack.append(operands[token](a,b))
            else:
                solution_stack.append(int(token))
        
        return solution_stack[0]


# cleaner version below:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        solution_stack = []
        for token in tokens:
            if token == "+":
                solution_stack.append(solution_stack.pop() + solution_stack.pop())
            elif token == "*":
                solution_stack.append(solution_stack.pop() * solution_stack.pop())
            elif token == "-":
                b = solution_stack.pop()
                a = solution_stack.pop()
                solution_stack.append(a - b)
            elif token == "/":
                b = solution_stack.pop()
                a = solution_stack.pop()
                solution_stack.append(int(a / b))
            else:
                solution_stack.append(int(token))
        
        return solution_stack[0]