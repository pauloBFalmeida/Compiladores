from lexic_analyser import CC20221Lexer, IllegalTokenError
from symbol_table import create_symbol_table


def exercicio_programa1(filename):

    # Read entry file
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

    lexer = CC20221Lexer()
    try:
        tokens = lexer.tokenize(data)
        symbol_table = create_symbol_table(tokens)
        print(tokens)
        print(symbol_table)
    except IllegalTokenError as error:
        print(error)

if __name__ == "__main__":
    # TODO: change this to use argparse
    import sys

    argv = sys.argv[1]
    exercicio_programa1(argv)
