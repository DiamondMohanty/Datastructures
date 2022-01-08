# Program to match check if all the tags in a html document are closed
# Author: Diamond Mohanty
# Date: 05-01-2022

from arraystack import ArrayStack

def is_balanced(raw_html: str) -> bool:
    stack = ArrayStack()
    
    for idx, ch in enumerate(raw_html):
        if  ch == '<':
            start = idx 
            end = raw_html.find('>', idx + 1)
            if end == -1:
                return False
            else:
                tag = raw_html[start:end+1].replace('/', '') # Incase it is a closing a tag so replace
                if stack.is_empty():
                    stack.push(tag)
                    continue

                if stack.top() == tag:
                    stack.pop()
                else:
                    stack.push(tag)
                start = 0
    return stack.is_empty()

        

# Test code
html = '''
<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>

</body>
'''
print(is_balanced(html))