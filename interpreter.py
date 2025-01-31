# interpreter.py
def interpret(ast, variables=None):
    if variables is None:
        variables = {}

    if ast[0] == 'program':
        for statement in ast[1]:
            interpret(statement, variables)
    elif ast[0] == 'print':
        print(ast[1].strip('"'))
    elif ast[0] == 'assign':
        variables[ast[1]] = ast[2]
    elif ast[0] == 'loop':
        for _ in range(variables[ast[1]]):
            interpret(ast[2], variables)
