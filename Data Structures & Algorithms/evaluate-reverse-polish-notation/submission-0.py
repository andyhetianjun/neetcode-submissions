class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                temp1 = stack.pop()
                temp2 = stack.pop()
                if tokens[i] == "+":
                    res = temp2 + temp1
                elif tokens[i] == "-":
                    res = temp2 - temp1
                elif tokens[i] == "*":
                    res = temp2 * temp1
                else:
                    if temp2 % temp1 != 0 and temp2 // temp1 < 0:
                        res = temp2 // temp1 + 1
                    else:
                        res = temp2 // temp1
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
