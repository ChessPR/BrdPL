import ply.lex as lex
import ply.yacc as yacc
import Board

reserved = {
    'Player':'TYPENAME',
    'Board' : 'TYPENAME',
    'Timer' : 'TYPENAME',
    'Dice' : 'TYPENAME',
    'Piece' : 'TYPENAME',
    'True' : 'BOOL',
    'False' : 'BOOL',
    'and' : 'AND',
    'or' : 'OR',
}

tokens = [
          'INT',
          'FLOAT',
          'WHITESPACE',
          'ID',
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

# reserved = {
#     'Player':'TYPENAME',
#     'True' : 'BOOL',
#     'False' : 'BOOL',
#     'and' : 'AND',
#     'or' : 'OR',
# }

t_ignore = r' '
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

def t_WHITESPACE(t):
    r'\s+'
    pass

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z\./]+'
    t.type = reserved.get(t.value, 'ID')
    if(t.type == 'BOOL'):
        if(t.value == 'True'):
            t.value = True
        else:
            t.value = False
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()

def p_main(p):
    '''
    main : prim
         | expression
         | empty
         | typedeclar
         | listprim
    '''
    print(run(p[1]))

def p_primitive(p):
    '''
    prim : BOOL
         | FLOAT
         | INT
         | ID
    '''
    p[0] = p[1]

def p_arg(p):
    '''
    args : LPAREN listprim RPAREN
         | LPAREN empty RPAREN
    '''
    p[0] = p[2]

def p_list_attr(p):
    '''
    listprim : prim COMMA listprim
            | prim
    '''
    try:
        p[0] = [p[1]]+p[3]
    except:
        p[0] = [p[1]]

def p_expression_prim(p):
    '''
        expression : prim MULTIPLY prim
                   | prim DIVIDE prim
                   | prim PLUS prim
                   | prim MINUS prim
                   | prim AND prim
                   | prim OR prim
                   | prim ISEQUALS prim
                   | prim GREATERTHAN prim
                   | prim GREATERTHANOREQUALS prim
                   | prim LESSTHAN prim
                   | prim LESSTHANOREQUALS prim
    '''
    p[0] = (p[2], p[1], p[3])

def p_typedeclar(p):
    '''
    typedeclar : TYPENAME
    '''
    print('typedeclar')
    p[0] = create_object(p[1],8,8,0,0,0)
    # else:
    #     p[0] = None
def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def create_object(typename, arg1, arg2, arg3, arg4, arg5):
    if typename == 'Board':
        print('create')
        return Board.Board(8,8)
    else:
        print('else')
        return None




env = {}

def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == 'and':
            return run(p[1]) and run(p[2])
        elif p[0] == 'or':
            return run(p[1]) or run(p[2])
    return p


parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)