class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for item in tokens:
            if item in ["+","-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()

                match item:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
            else:
                stack.append(int(item))

        return stack[0]