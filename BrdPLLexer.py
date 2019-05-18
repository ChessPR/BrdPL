import ply.lex as lex
import ply.yacc as yacc
import Board
import Dice
import Player
import Timer
import Piece
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
    'CountDown' : 'FUNCTION',
    'Display' : 'DISPLAY',
    'DiceRollGame' : 'DICEROLLGAME',
}

tokens = [
          'INT',
          'FLOAT',
          'STRING',
          'WHITESPACE',
          'ID',
          'PLUS',
          'MINUS',
          'DIVIDE',
          'MULTIPLY',
          'EQUALS',
          'COMMA',
          'SEMI',
          'POINT',
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

t_ignore = r' '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_COMMA = ','
t_SEMI = ';'
t_POINT = '.'
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

def t_STRING(t): # have to use ""
    r'\".*?\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print('Line %d: Error with value %s' % (t.lineno, t.value))
    return t


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()


# Grammar of the code
def p_main(p):
    '''
    main : prim
         | expression
         | empty
         | typedeclar
         | listprim
         | var_assign
         | var
         | display
         | diceRollGame
    '''
    print(run(p[1]))

def p_primitive(p):
    '''
    prim : BOOL
         | FLOAT
         | INT
         | ID
         | STRING
    '''
    p[0] = p[1]

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
    typedeclar : TYPENAME LPAREN empty RPAREN SEMI
               | TYPENAME LPAREN listprim RPAREN SEMI
    '''
    print('typedeclar')
    if len(p[3]) == 2:
        p[0] = create_object(p[1],(p[3])[0],(p[3])[1],0,0,0)
    elif len(p[3]) == 3:
        p[0] = create_object(p[1],(p[3])[0],(p[3])[1],(p[3])[2],0,0)
    elif len(p[3]) == 3:
        p[0] = create_object(p[1], (p[3])[0], (p[3])[1], (p[3])[2], 0, 0)
    else:
        p[0] = None

def p_fun_call(p):
    '''
    expression : FUNCTION LPAREN empty RPAREN SEMI
               | var POINT FUNCTION LPAREN listprim RPAREN SEMI
    '''
    print('hi')


def p_forced_display(p):
    '''
    display : DISPLAY
    '''
    board = Board.Board(8, 8)
    b = board.createChessBoard("white", "black")
    board.display(b[0], 800, 800, b[1])
    p[0] = "Running"

# Varable declaration requires semi-colon at the end.
def p_var_assign(p):
    '''
    var_assign : ID EQUALS expression SEMI
               | ID EQUALS prim SEMI
               | ID EQUALS typedeclar SEMI
    '''
    # Build our tree
    p[0] = ('=', p[1], p[3])

def p_expression_var(p):
    '''
    var : ID
    '''
    p[0] = ('var', p[1])

def p_diceGame(p):
    '''
    diceRollGame : DICEROLLGAME SEMI
    '''
    dice = Dice.Dice(2,6)
    print('Roll Dice Game')
    print('')
    player1 = sum(dice.roll())
    player2 = sum(dice.roll())
    print(('Player 1 score: %d   Player 2 score: %d') % (player1,player2))
    if player1 > player2:
        print('Player 1 Won!!!')
    elif player1 < player2:
        print('Player 2 Won!!!')
    else:
        print('Is a Tie!!!')
    p[0] = ''

def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

# Helper method for the creation of objects,
def create_object(typename, arg1, arg2, arg3, arg4, arg5):
    if typename == 'Board':
        print('Board Created')
        return Board.Board(arg1,arg2)
    elif typename == 'Dice':
        print('Dice Created')
        return Dice.Dice(arg1, arg2)
    elif typename == 'Player':
        print('Player Created')
        return Player.Player(arg1, arg2, arg3)
    elif typename == 'Timer':
        print('Timer Created')
        return Timer.Timer(arg1, arg2, arg3)
    elif typename == 'Piece':
        print('Piece Created')
        return Piece.Piece(arg1, arg2, arg3,arg4,arg5)
    else:
        print('else')
        return None

env = {}

def run(p):
    global env
    if p in env: # Fixes problem with the variable declaration
        return env[p]
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
        elif p[0] == '=':
            env[p[1]] = run(p[2])
            return ''
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
    return p


parser = yacc.yacc()

while True:
    try:
        s = input('>>>')
    except EOFError:
        break
    parser.parse(s)