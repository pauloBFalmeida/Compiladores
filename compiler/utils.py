from dataclasses import dataclass
from typing import Dict, List

from compiler.ply.lex import LexToken

TYPES_TO_STORE = ["IDENT"]


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
    for i, token in enumerate(tokens):
        if token.type in TYPES_TO_STORE:  # type: ignore
            if token.value not in symbol_table:  # type: ignore
                symbol_table[token.value] = SymbolTableEntry(  # type: ignore
                    var_name=token.value,  # type: ignore
                    token_id=i,
                    line_declared=token.lineno,  # type: ignore
                    lines_referenced=[],
                )
            else:
                symbol_table[token.value].lines_referenced.append(token.lineno)  # type: ignore
    return symbol_table
