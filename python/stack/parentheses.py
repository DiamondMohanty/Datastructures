# Check if the parentheses are in order
# Author: Diamond Mohanty
# Date: 05-Jan-2022

# Correct Order of Parentheses: ({[

from arraystack import ArrayStack
def is_matched(expression: str) -> bool:
  
    stack = ArrayStack()
    for ch in expression:

        if stack.is_empty():    # boundary condition
            stack.push(ch)
            continue

        if ((stack.top() == '[' and ch == ']') or
        (stack.top() == '{' and ch == '}') or
        (stack.top() == '(' and ch == ')')):
            stack.pop()
        else:
            stack.push(ch)

    return stack.is_empty()


# Test Code
sample1 = '()(()){([()])}'
sample2 = '((()(()){([()])}))'
sample3 = ')(()){([()])}'
sample4 = '({[])}'
sample5 = '('

samples = [sample1, sample2, sample3, sample4, sample5]
for sample in samples:
    print(is_matched(sample))
