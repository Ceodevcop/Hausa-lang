import ply.lex as lex

tokens = (
    'FARA',
    'KARSHE',
    'RUBUTA',
    'LAMBA',
    'DAIDAI',
    'IDAN',
    'SAU',
    'NUMBER',
    'STRING',
)

t_FARA = r'fara'
t_KARSHE = r'karshe'
t_RUBUTA = r'rubuta'
t_LAMBA = r'lamba'
t_DAIDAI = r'daidai'
t_IDAN = r'idan'
t_SAU = r'sau'
t_STRING = r'"[^"]*"'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
