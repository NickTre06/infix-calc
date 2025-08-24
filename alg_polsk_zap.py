import re


def is_float(element: any) -> bool:
    return re.match(r'^-?\d+(?:\.\d+)$', element) is not None

def infix_to_rpn(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        'sin': 3  # sin имеет высокий приоритет, чтобы выполняться раньше остальных операций
    }
    
    output = []
    stack = []
    
    def is_function(token):
        """Проверяем, является ли токен функцией"""
        return token.lower() in ['sin']
    
    for token in expression:
        if is_float(token):  # Число
            output.append(token)
        elif token in precedence.keys():  # Бинарный оператор
            while (stack and stack[-1] != '(' and
                  precedence.get(stack[-1], 0) >= precedence.get(token)):
                output.append(stack.pop())
            stack.append(token)
        elif is_function(token):  # Функция типа sin
            stack.append(token)
        elif token == '(':  # Открывающая скобка
            stack.append(token)
        elif token == ')':  # Закрывающая скобка
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Удаляем открывающую скобку
            if stack and is_function(stack[-1]):
                output.append(stack.pop())  # Выталкиваем функцию
                
    while stack:
        output.append(stack.pop())
        
    return ' '.join(output)