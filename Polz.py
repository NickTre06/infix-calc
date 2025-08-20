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


# Тестируем функцию
expression =  "31+5*(7^2)"
result = parse_math_expression(expression)
for idx, element in result:
    print(f"{idx}: {element}")