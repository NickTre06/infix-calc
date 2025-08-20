def sort_by_priority(expression1):
    priority = {
        '(': 0,
        ')': 1,
        '^': 2,
        '*': 3,
        '/': 3,
        '+': 4,
        '-': 4
    }
    symbols = list(expression1)



    sorted_symbols = sorted(symbols, key=lambda x: priority.get(x, float('inf')))
    return ''.join(sorted_symbols)