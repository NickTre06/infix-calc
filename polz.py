def isSystemSymbol(num_buffer, symbol):
    if symbol == 'a':
        return true;
    return false;

def isVariable(num_buffer, symbol):
    if symbol == 's':
        return true;
    return false;

def parse_math_expression(expression):
    elements = []
    i = 0

    def add_element(value):
        nonlocal i
        elements.append((i, value))
        i += 1




    # Пробегаем по строке символ за символом
    num_buffer = ''
    for char in expression:
        #if char.isdigit() or char == '.' or isSystemSymbol(num_buffer, char) or isVariable(num_buffer, char):
        if char.isdigit() or char == '.':
            num_buffer += char
        else:
            if num_buffer:
                add_element(num_buffer)
                num_buffer = ''  # Очищаем буфер

            # Добавляем оператор или скобку
            if char != ' ':  # Пропускаем пробелы
                add_element(char)

    # Если в конце строки остался незавершённый числовой токен
    if num_buffer:
        add_element((num_buffer))

    return elements


