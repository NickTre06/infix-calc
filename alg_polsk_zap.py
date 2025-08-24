import re


def is_float(element: any) -> bool:
    return re.match(r'^-?\d+(?:\.\d+)$', element) is not None

def infix_to_rpn(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,   
        '^': 3,    
        'sin': 4, 
        'cos': 4,
        'tan': 4,  
        'sqrt': 4, 
        'log': 4,  
        'exp': 4, 
        'abs': 4,  
    }
    
    
    output = []
    stack = []
    
    def is_function(token):
        """Проверяем, является ли токен функцией"""
        return token.lower() in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'abs']
    
    for token in expression:
        if token.isdigit() or is_float(token):  
            output.append(token)
        elif token in precedence.keys():  
            while (stack and stack[-1] != '(' and
                  precedence.get(stack[-1], 0) >= precedence.get(token)):
                output.append(stack.pop())
            stack.append(token)
        elif is_function(token):  
            stack.append(token)
        elif token == '(':  
            stack.append(token)
        elif token == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
            if stack and is_function(stack[-1]):
                output.append(stack.pop())  
                
    while stack:
        output.append(stack.pop())
        
    return output