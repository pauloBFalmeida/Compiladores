"""
Trabalho de Compiladores 2022-1

Integrantes:
    * Helena Aires
    * Paola Abel
    * Paulo Almeida
    * Pedro Aquino

Exercício-Programa 1: Analisador Léxico 
Exercício-Programa 2: Analisador Sintático
"""

from pathlib import Path

from compiler.lexical_analyzer import CC20221Lexer, IllegalTokenError
from compiler.syntactic_analyzer import CC20221SyntacticAnalyzer
from compiler.utils import SymbolTable, create_symbol_table


def exercicio_programa1(source_code: str) -> None:
    """Analisador léxico"""
    lexer = CC20221Lexer()

    tokens = []
    symbol_table: SymbolTable = {}

    try:
        tokens = lexer.tokenize(source_code)
        symbol_table = create_symbol_table(tokens)
    except IllegalTokenError as error:
        print(error)

    if tokens:
        for tok in tokens:
            print(tok)
    if symbol_table:
        for row in symbol_table.values():
            print(row)


def exercicio_programa2(source_code: str) -> None:
    """Analisador sintático"""
    parser = CC20221SyntacticAnalyzer()
    output = parser.parse(source_code)
    print(output)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    s = None

    try:
        with (Path(__file__).parent / f"{filename}").open("r") as f:
            s = f.read()
    except (FileNotFoundError, IndexError):
        print("Favor inserir um nome de arquivo válido :(")
    
    if s:        
        if sys.argv[2] == "lexical":
            exercicio_programa1(s)
        elif sys.argv[2] == "syntactic":
            exercicio_programa2(s)
        else:
            print("Essa tarefa ainda não foi implementada :(")