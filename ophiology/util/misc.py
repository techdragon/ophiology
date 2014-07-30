"""Miscelaneous functions."""

def message_level_from_code(code):
    char = code[1:]
    if char == 'R':
        return 'Refactor'
    elif char == 'C':
        return 'Convention'
    elif char == 'W':
        return 'Warning'
    elif char == 'E':
        return 'Error'
    elif char == 'F':
        return 'Fatal'
    else:
        return ''
