# cli.py
import sys
from parser import parser
from interpreter import interpret

def run_program(filename):
    with open(filename, 'r') as file:
        code = file.read()
    ast = parser.parse(code)
    interpret(ast)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Yi amfani da: python cli.py shirin.hausa")
    else:
        filename = sys.argv[1]
        run_program(filename)
