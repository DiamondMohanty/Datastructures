# Program to reverse the lines of a given text
# Author: Diamond Mohanty
# Date: 05-Jan-2022

from arraystack import ArrayStack
def reverse(text: str) -> str:
    # Considering . is a line separtor
    lines = text.split('.')

    stack = ArrayStack()
    for line in lines:
        stack.push(line.strip())

    output = []
    while not stack.is_empty():
        output.append(stack.pop())
    
    return output[0] + '.'.join(output[1:]) + '.' # Removes . in the begining and adds . to the end


# Test Code
sample_text = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
'''
reversed = reverse(sample_text)
print('Input {0}'.format(sample_text))
print('Output {0}'.format(reversed))