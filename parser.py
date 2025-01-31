import ply.yacc as yacc

def p_program(p):
    '''
    program : FARA statement_list KARSHE
    '''
    p[0] = ('program', p[2])

def p_statement_list(p):
    '''
    statement_list : statement
                  | statement statement_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement(p):
    '''
    statement : RUBUTA STRING
              | LAMBA IDENTIFIER DAIDAI NUMBER
              | SAU IDENTIFIER statement_list KARSHE
    '''
    if p[1] == 'rubuta':
        p[0] = ('print', p[2])
    elif p[1] == 'lamba':
        p[0] = ('assign', p[2], p[4])
    elif p[1] == 'sau':
        p[0] = ('loop', p[2], p[3])

def p_error(p):
    print("Syntax error!")

parser = yacc.yacc()
