Recalled Stack and solved the problem of checking if a given string of parentheses is balanced or not. The code uses a stack data structure to keep track of opening parentheses. It iterates through the string, pushing opening parentheses onto the stack and popping them when a matching closing parenthesis is found. If the stack is empty at the end, the string is balanced; otherwise, it is not. The result is printed accordingly.



s = "({[]})"
stack = []
for ch in s:
    if ch =='(' or ch =="{" or ch =="[":
        stack.append(ch)
    else:
        if len(stack) == 0:
            print("Not Balanced")
            break
    top = stack.pop()
    if (ch == ")" and top != "(" ) or (ch == "}" and top != "{") or (ch == "]" and top != "["):
        print("Not Balanced")
        break
    else:
        if len(stack) == 0:
            print("Balanced")
        else:
            print("Not Balanced")
            
            
Given tokens of an RPN expression (e.g., ["2","1","+","3","*"]), use a list as a stack to compute the result.
and Started learning about Locators 

tokens = ["2", "1", "+", "3", "*"]
stack = []
for ch in tokens:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(int(a / b))
print(stack[0])

