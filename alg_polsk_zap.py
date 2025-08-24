import re


def is_float(element: any) -> bool:
    return re.match(r'^-?\d+(?:\.\d+)$', element) is not None

def infix_to_rpn(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,    # Остаток от деления
        '^': 3,    # Возведение в степень
        'sin': 4,  # Тригонометрическая функция
        'cos': 4,
        'tan': 4,  # Тангенс сокращённо записан как tan
        'sqrt': 4, # Квадратный корень
        'log': 4,  # Логарифм
        'exp': 4,  # Экспонента e^x
        'abs': 4,  # Модуль числа
    }
    
    
    output = []
    stack = []
    
    def is_function(token):
        """Проверяем, является ли токен функцией"""
        return token.lower() in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'abs']
    
    for token in expression:
        if token.isdigit() or is_float(token):  # Число
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
        
    return output