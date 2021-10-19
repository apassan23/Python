# importing Stack class
from stack import Stack

# function to evaluate postfix expn
# @param exp: str
# OUTPUT: float|int
def evalPostFix(exp):
    opStack = Stack()

    # trivial case
    if exp[-1].isdigit():
        print("Invalid Expression!")
        return

    for element in exp:
        if element.isdigit():
            opStack.push(element)
        else:
            # expn is incorrect any time if there are not
            # exactly 2 operands in stack
            if opStack.size() != 2:
                print("Invalid Expression!")
                return
            else:
                op2 = opStack.pop()
                op1 = opStack.pop()
                try:
                    opStack.push(str(eval(op1 + element + op2)))
                except SyntaxError:
                    print("Invalid operator '{}' provided!".format(element))
                    return

    return opStack.pop()

# function to check for matching parenthesis
# @param exp: str
# OUTPUT: bool
def checkParenthesis(exp):
    stack = Stack()
    # dictionary for matching brackets
    matches = {'}': '{', ']': '[', ')': '('}
    for element in exp:
        # element is a opening bracket
        if element in matches.values():
            stack.push(element)
        # element is a closing bracket
        elif element in matches.keys():
            if stack.isEmpty() or (stack.pop() != matches.get(element)):
                return False
    # brackets do not match if there is still
    # a bracket in stack
    return stack.isEmpty()

# function to convert infix to postfix
# @param infixExp: str
# OUTPUT: str
def toPostFix(infixExp):
    postfix = ''
    stack = Stack()
    # dictionary for precedence of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for element in infixExp:
        # element is operand
        if element.isalpha():
            postfix += element
        elif element == '(':
            stack.push(element)
        elif element == ')':
            # sub expression is completed, so append all
            # operators
            while(not(stack.isEmpty()) and stack.peek() != '('):
                postfix += stack.pop()
            if not(stack.isEmpty()) and stack.peek() != '(':
                return -1
            # popping the leftover '('
            else:
                stack.pop()
        # element is operator
        else:
            # if the operator has a higher priority than operators
            # already present n the stack
            while(not(stack.isEmpty()) and (precedence[element] <= precedence.get(stack.peek(), -1))):
                postfix += stack.pop()
            # push the operator
            stack.push(element)
    # pop the leftover operators from the stack and append them
    while not(stack.isEmpty()):
        postfix += stack.pop()

    return postfix

# taking input
print("What You want to do?")
print("1. Evaluate Postfix Expression")
print("2. Check if the parenthesis match")
print("3. Convert Infix Expression to Postfix Expression")
choice = int(input("Choose: "))
exp = input("Enter Expression: ")

if choice == 1:
    print("Result: {}".format(evalPostFix(exp)))
elif choice == 2:
    if checkParenthesis(exp):
        print("Parenthesis Match!")
    else:
        print("Parenthesis do not match!")
elif choice == 3:
    print("PostFix expression: {}".format(toPostFix(exp)))
else:
    print("Invalid Choice!")