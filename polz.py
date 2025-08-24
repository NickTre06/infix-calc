import math
from collections import deque
CONSTANTS = {"M_PI": math.pi, "M_E": math.e}


def isConstant(token):
    
    return token in CONSTANTS

def check_brackets_balance(line):
  
    stack = deque()
    for ch in line:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
    
    return len(stack) == 0



def isFunction(token):
    return token in FUNCTIONS


def getTokenType(char):
    """Вычисляет тип токена"""
    if char.isdigit() or char == '.':
        return 'digit' 
    elif char.isalpha():
        return 'word'  
    elif char == '(' or char == ')':
        return 'bracket'
    elif char.isspace():
        return 'space'
    else:
        return 'operation'  
    


def parse_math_expression(expression):
    elements = []
    index = 0

    def add_element(value):
        nonlocal index
        elements.append(value)
        index += 1

    buf = ''

    if len(expression) < 1:
        raise ValueError("Некорректная исходная строка")

    prev_token_type = None
    current_token_type = getTokenType(expression[0])
    buf += expression[0]
    if current_token_type == 'bracket':
        add_element(expression[0])
        buf = ''
        

    for char in expression[1:]:
        prev_token_type = current_token_type
        current_token_type = getTokenType(char)

        if current_token_type == 'bracket':
            if buf and prev_token_type != 'space':
                add_element(buf)
            add_element(char)
            buf = ''
            continue

        if prev_token_type == 'word' and current_token_type == 'digit':
            current_token_type = 'word'

        if prev_token_type == current_token_type :
            buf += char
        else:
           
            if buf and prev_token_type != 'space':
                add_element(buf)
            buf = char 

   
    if buf:
        add_element(buf)

    return elements
    












