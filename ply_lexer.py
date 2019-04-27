# this is a try in ply
import ply.lex as lex
import ply.yacc as yacc
import sys

# Create a list to hold all of the token names

reserved = {
    # 'if' : 'IF',
    # 'then' : 'THEN',
    # 'else' : 'ELSE',
    # 'while' : 'WHILE',
    # 'board' : 'BOARD',
    # 'player' : 'PLAYER',
    # 'timer' : 'TIMER',
    # 'dice' : 'DICE',
    # 'piece' : 'PIECE',
    # 'print' : 'PRINT',
    # 'for' : 'FOR',
    'True' : 'TRUE',
    'False' : 'FALSE',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT'

}

tokens = [
    'INT',
    'FLOAT',
    'STRING',
    'NAME', # Identifier
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    # 'LPAREN',
    # 'RPAREN',
    # 'LBRACKET',
    # 'RBRACKET',
    # 'LSBRACKET',
    # 'RSBRACKET',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSTHANOREQUALS',
    'GREATERTHANOREQUALS',
    'ISEQUALS',

    ] + list(reserved.values())

# Use regular expressions to define what each token is
# Alternatively : literals = [ '+','-','*','/' ] or  literals = "+-*/"
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_ISEQUALS = r'\=\='
t_EQUALS = r'\='
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACKET = r'\{'
# t_RBRACKET = r'\}'
# t_LSBRACKET = r'\['
# t_RSBRACKET = r'\]'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSTHANOREQUALS = r'\<\='
t_GREATERTHANOREQUALS = r'\>\='


# Ply's special t_ignore variable allows us to define characters the lexer will ignore.
# We're ignoring spaces.
t_ignore = r' '

# More complicated tokens, such as tokens that are more than 1 character in length
# are defined using functions.
# A float is 1 or more numbers followed by a dot (.) followed by 1 or more numbers again.


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# An int is 1 or more numbers.
def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Line %d: Error with value %s' % (t.lineno, t.value))
    return t

def t_STRING(t):
    r'\".*?\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print('Line %d: Error with value %s' % (t.lineno, t.value))
    return t
# A NAME is a variable name. A variable can be 1 or more characters in length.
# The first character must be in the ranges a-z A-Z or be an underscore.
# Any character following the first character can be a-z A-Z 0-9 or an underscore.
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
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
    ('left', 'OR', 'AND'),

)

# Define our grammar. We allow expressions, var_assign's and empty's.
def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
         | bool_statement
         | bool_and_or
    '''
    print(run(p[1]))

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
               | NAME EQUALS bool_statement
               | NAME EQUALS STRING
               | NAME EQUALS bool_and_or
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
               | expression ISEQUALS expression
               | expression GREATERTHAN expression
               | expression GREATERTHANOREQUALS expression
               | expression LESSTHAN expression
               | expression LESSTHANOREQUALS expression
    '''
    # Build our tree.
    p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_bool_statement(p):
    '''
    bool_statement : TRUE
                   | FALSE
    '''
    # if p[1] == 'True':
    #     p[0] = True
    # elif p[1] == 'False':
    #     p[0] = False
    p[0] = p[1]


def p_bool_and_or_operations(p):
    '''
    bool_and_or : bool_statement
                | bool_statement AND bool_statement
                | bool_statement OR bool_statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    # elif p[2] == 'And':
    #     p[0] = p[1] and p[3]
    # elif p[2] == 'Or':
    #     p[0] = p[1] or p[3]
    elif p[2] == 'and' or p[2] == 'or':
        p[0] = (p[2], p[1], p[3])

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

# def p_

# Output to the user that there is an error in the input as it doesn't conform to our grammar.
# p_error is another special Ply function.
def p_error(p):
    print("Syntax error found!") # Standard error message

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

# Build the parser
parser = yacc.yacc()
# Create the environment upon which we will store and retreive variables from.
env = {}
# The run function is our recursive function that 'walks' the tree generated by our parser.
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
        elif not p[0] and True:
            return False
        elif p[0] and True:
            return True
        elif p[0] == 'and':
            return run(p[1]) and run(p[2])
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
    else:
        return p

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)
