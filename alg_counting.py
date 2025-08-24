import math
from collections import deque

def sum(a,b):
    return a + b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def remains(a,b):
    return a%b
def division(a,b):
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
    return math.sqrt(x)
def expon(x):
    return math.exp(x)
def abss(x):
    return math.abs(x)
def logarifm(base,arg):
    return math.log(arg, base)





def alg_count(rpn_expression):

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
            # Пробуем превратить токен в число
            number = float(token)
            stack.append(number)
        except ValueError:
            # Если токен не число, считаем, что это оператор или функция
            if token in operators:
                op_func = operators[token]
                num_args = len(op_func.__code__.co_varnames)  # Узнаём кол-во аргументов функции
                args = [stack.pop() for _ in range(num_args)]  # Берём аргументы из стека
                result = op_func(*reversed(args))  # Применяем функцию к аргументам
                stack.append(result)  # Записываем результат обратно в стек
            else:
                raise ValueError(f'Неопознанный символ {token}')
    
    if len(stack) > 1:
        raise ValueError('Ошибка в выражении')
    
    return stack.pop()

    