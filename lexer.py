import ply.lex as lex


tokens = [
    'ID',
    'INT',
    'FLOAT'
    'CHARACTER',
    'DELIMITER',
    'OPERATOR',
    'KEYWORD',
]

t_ID = '[a-zA-z_][a-zA-z_0-9]+'
t_CHARACTER = '[a-zAz]'
t_DELIMITER = [r'\+', r'\-', ]
t_OPETATOR = r'\[+-*/=]'

t_ignore = r' ' # We are going to ignore spaces

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Skips ilegal argument
def t_error(t):
    print('Ilegal argument!')
    lexer.skip(1)

lexer = lex.lex()