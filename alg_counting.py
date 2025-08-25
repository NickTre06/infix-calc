import math
from collections import deque

def sum(a,b):
    return a + b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def remains(a,b):
    if b==0:
       raise Exception("ошибка в условии") 
    return a%b
def division(a,b):
    if b==0:
        raise Exception("ошибка в условии") 
    return a/b
def powra(a,b):
    return pow(a, b)
def sinus(x):
    return math.sin(x)
def cosin(x):
    return math.cos(x)
def tang(x):
    return math.tan(x)
def sqrtu(x):
    if x < 0:
        raise Exception("ошибка в условии") 
    return math.sqrt(x)
def expon(x):
    return math.exp(x)
def abss(x):
    return math.abs(x)
def logarifm(base,arg):
    if (arg == 1) or (arg <= 0) or (base <= 0):
         raise Exception("ошибка в условии")  
    return math.log(arg, base)


def is_variables(element: any, variables: any) -> bool:
    for defin in variables:
        if defin == element:
            return True
    return False



def alg_count(rpn_expression, variables):

    stack = deque()
    
    operators = {
        '+': sum,
        '-': subtraction,
        '*': multiply,
        '/': division,
        '%': remains,
        '^': powra,
        'sin': sinus,
        'cos': cosin,
        'tan': tang,
        'sqrt': sqrtu,
        'exp': expon,
        'abs': abss,
        'log': logarifm,
      
         }
    stack = deque()
    tokens = rpn_expression
    
    for token in tokens:
        try:
           
            number = None
            if token == 'M_PI':
                number = math.pi
            elif token == 'M_E':
                number = math.e
            elif is_variables(token , variables):
                number = float(variables[token])
            else:
                number = float(token)
            stack.append(number)
        except ValueError:
            
            if token in operators:
                op_func = operators[token]
                num_args = len(op_func.__code__.co_varnames)  
                args = [stack.pop() for _ in range(num_args)]  
                result = op_func(*reversed(args)) 
                stack.append(result)  
            else:
                raise ValueError(f'Неопознанный символ {token}')
    
    if len(stack) > 1:
        raise ValueError('Ошибка в выражении')
    
    return stack.pop()

    