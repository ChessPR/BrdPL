import ply.lex as lex
import ply.yacc as yacc
import Board
# Create a list to hold all of the token names
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    # 'player' : 'PLAYER',
    # 'timer' : 'TIMER',
    # 'dice' : 'DICE',
    # 'piece' : 'PIECE',
    'Board' : 'BOARD',
    'print' : 'PRINT',
    'for' : 'FOR',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT'

}
tokens = [

    'INT',
    'FLOAT',
    'TRUE',
    'FALSE',
    # 'BOARD',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LSBRACKET',
    'RSBRACKET',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSTHANOREQUALS',
    'GREATERTHANOREQUALS',
    'ISEQUALS',


] + list(reserved.values())

# Use regular expressions to define what each token is
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_COMMA = ','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSTHANOREQUALS = r'\<\='
t_GREATERTHANOREQUALS = r'\>\='

t_ignore = r' '

# def t_Board(t):
#     'Board'
#     return str('Board')

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# An int is 1 or more numbers.
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TRUE(t):
    'True'
    t.value = True
    return t

def t_FALSE(t):
    'False'
    t.value = False
    return t

# A NAME is a variable name. A variable can be 1 or more characters in length.
# The first character must be in the ranges a-z A-Z or be an underscore.
# Any character following the first character can be a-z A-Z 0-9 or an underscore.
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if str(t.value) in tokens or str(t.value) in reserved.values():
        pass
    t.type = 'NAME'
    return t

# Skip the current token and output 'Illegal characters' using the special Ply t_error function.
def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Ensure our parser understands the correct order of operations.
# The precedence variable is a special Ply variable.
precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'OR', 'AND')

)

# Define our grammar. We allow expressions, var_assign's and empty's.
def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
         | board
    '''
    # print(p[1])
    print(run(p[1])) #print((p[1])) # with print(p[1]) I can see the tuple

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    # Build our tree
    p[0] = ('=', p[1], p[3])

# Expressions are recursive.
def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
               | expression AND expression
               | expression OR expression
               | expression ISEQUALS expression
               | expression GREATERTHAN expression
               | expression GREATERTHANOREQUALS expression
               | expression LESSTHAN expression
               | expression LESSTHANOREQUALS expression
    '''
    # Build our tree.
    p[0] = (p[2], p[1], p[3])

# def p_expression_and_or_bool(p):
#     '''
#     expression_and_or : NAME AND NAME
#                       | NAME OR NAME
#     '''
#     p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_bool(p):
    '''
    expression : TRUE
               | FALSE
    '''
    if  p[1] == True:
        p[0] = True
    elif p[1] == False:
        p[0] = False

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

def p_board(p):
    '''
    board : BOARD
    '''
    print('hi')


# Output to the user that there is an error in the input as it doesn't conform to our grammar.
# p_error is another special Ply function.
def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
            return ''
        elif p[0] == '==':
            return run(p[1]) == run(p[2])
        elif p[0] == '<':
            return run(p[1]) < run(p[2])
        elif p[0] == '>':
            return run(p[1]) > run(p[2])
        elif p[0] == '<=':
            return run(p[1]) <= run(p[2])
        elif p[0] == '>=':
            return run(p[1]) >= run(p[2])
        # elif p[1] == 'True':
        #     return True
        # elif p[1] == 'False':
        #     return False
        elif p[0] == 'and':
            return run(p[1]) and run(p[2])
        elif p[0] == 'or':
            return run(p[1]) or run(p[2])
        elif p[1] == 'Board':
            print('me quiero matar')
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
    return p

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)