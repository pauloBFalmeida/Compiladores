from dataclasses import dataclass
from typing import Dict, List

from ply.lex import LexToken


TYPES_TO_STORE = [
    "IDENT",
    "INT_CONSTANT",
    "FLOAT_CONSTANT",
    "STRING_CONSTANT",
]


@dataclass
class SymbolTableEntry:
    var_name: str
    token_id: int
    line_declared: int
    lines_referenced: List[int]
    var_type: str = "Unknown"


SymbolTable = Dict[str, SymbolTableEntry]


def create_symbol_table(tokens: List[LexToken]) -> SymbolTable:
    """Create symbol table from tokens read in source code"""
    symbol_table: SymbolTable = {}
    for id, token in enumerate(tokens):
        if token.type in TYPES_TO_STORE:
            if token.value not in symbol_table:
                symbol_table[token.value] = SymbolTableEntry(
                    var_name=token.value,
                    token_id=id,
                    line_declared=token.lineno,
                    lines_referenced=[],
                )
            else:
                symbol_table[token.value].lines_referenced.append(token.lineno)
    return symbol_table
