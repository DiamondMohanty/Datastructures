# Program to evaluate an given expression
# Author: Diamond Mohanty
# Date: 05-01-2022

#TODO: Precedance of all the operators is considered as same. Check the precedence before evaluation

from arraystack import ArrayStack

class DivideZero(Exception):
    pass

class UnbalancedExpression(Exception):
    pass

def result(lhs, rhs, operator):
    if operator == '+':
        return lhs + rhs
    elif operator == '-':
        return lhs - rhs
    elif operator == '*':
        return lhs * rhs
    elif operator == '/':
        if rhs == 0:
            raise DivideZero('Divide by zero')
        else:
            return lhs/rhs

def evaluate(expression):
    expression = '(' + expression.replace(' ', '') + ')'
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    idx = 0
    while idx < len(expression):
        ch = expression[idx]
        if ch in ['+', '-', '*', '/']:
            operator_stack.push(ch)
            idx += 1
        elif ch == '(':
            operator_stack.push(ch)
            idx += 1
        elif ch == ')':
            j_token = operator_stack.pop()
            while j_token != '(':
                if j_token in ['+', '-', '*', '/']:
                    operator = j_token        
                    lhs = float(operand_stack.pop())
                    rhs = float(operand_stack.pop())
                    operand_stack.push(result(lhs, rhs, operator))
                j_token = operator_stack.pop()
            idx += 1
        else:
            token = ch
            j_idx = idx + 1
            while expression[j_idx] not in ['(', ')', '+', '-', '*', '/']:
                # For multidigit numbers
                token += expression[j_idx]
                j_idx += 1
            operand_stack.push(token)
            idx = j_idx
    
    if not operator_stack.is_empty():
        raise UnbalancedExpression('Expression is not balanced')
    return operand_stack.pop()

# Test Code
expression = '100 * ( 2 + 12 - 10 )'
result = evaluate(expression)
print(result)