from lexic_analyser import CC20221Lexer, IllegalTokenError
from symbol_table import SymbolTable, create_symbol_table


def exercicio_programa1(filename):

    # Read entry file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    lexer = CC20221Lexer()

    tokens = []
    symbol_table: SymbolTable = {}

    try:
        tokens = lexer.tokenize(data)
        symbol_table = create_symbol_table(tokens)
    except IllegalTokenError as error:
        print(error)
    
    if tokens:
        for tok in tokens:
            print(tok)
    if symbol_table:
        for row in symbol_table.values():
            print(row)


if __name__ == "__main__":
    # TODO: change this to use argparse
    import sys

    try:
        argv = sys.argv[1]
        exercicio_programa1(argv)
    except (IndexError, FileNotFoundError):
        print("File not found! Try again with a valid file name :)")