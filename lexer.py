import ply.lex as lex


tokens = [
    'ID',
    'INT',
    'FLOAT'
    'CHARACTER',
    'DELIMITER',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'LESS_THAN',
    'MORE_THAN',
    'LESS_EQUAL',
    'MORE_EQUAL',
    'NOT_EQUAL',
    'EQUALS'
    'KEYWORD',
]

t_ID = '[a-zA-z_][a-zA-z_0-9]+'
# t_CHARACTER = '[a-zAz]'
# t_DELIMITER = r'\+', r'\-'
# t_OPETATOR = r'\[+-*/=]'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
# t_KEYWORD = '(Board|Player|Dice|Timer)'

t_ignore = r' ' # We are going to ignore spaces

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Skips ilegal argument
def t_error(t):
    print('Ilegal argument!')
    lexer.skip(1)


lexer = lex.lex()

# lexer.input("abc = 1")
#
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
