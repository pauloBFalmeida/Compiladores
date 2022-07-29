import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

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


@dataclass
class TableEntry:
    identifier: str
    datatype: str
    dimensions: List[int]
    line: int


class Scope:

    def __init__(self, parent_scope: Optional["Scope"] = None, is_loop: bool = False) -> None:
        self.table: List[TableEntry] = []
        self.inner_scopes: List["Scope"] = []
        self.is_loop = is_loop
        self.parent_scope = parent_scope

    def add_table_entry(self, entry: TableEntry) -> None:
        # Assert not already in scope
        if entry.identifier in [e.identifier for e in self.table]:
            raise IdentifierAlreadyInScopeError(
                f"Variable already declared in line {entry.line}"
                )
        self.table.append(entry)

    def add_to_inner(self, scope: "Scope"):
        self.inner_scopes.append(scope)


class ScopeStack:
    def __init__(self):
        self.stack: List[Scope] = []

    def pop(self) -> Scope:
        return self.stack.pop()

    def push(self, scope: Scope) -> None:
        self.stack.append(scope)

    def peek(self) -> Scope:
        return self.stack[-1] if self.stack else None


class Node:
    def __init__(self, left: Optional['Node'], right: Optional['node'],
                 value: Optional[Union[str, int, float]], result_type: str):
        self.left = left
        self.right = right
        self.value = value
        self.result_type = result_type
        self.id = uuid.uuid4()

    def as_json(self) -> Dict:
        """Recursively build sub-tree"""
        left = None
        if self.left is not None:
            left = self.left.as_json()

        right = None
        if self.right is not None:
            right = self.right.as_json()

        return {
            'value': self.value,
            'left': left,
            'right': right
        }

    def __str__(self):
        return f'<NodeId: {self.id}>'


class IdentifierAlreadyInScopeError(Exception):
    pass

class BreakOutsideLoopError(Exception):
    pass

class VariableNotDeclaredError(Exception):
    pass

class InvalidTypeOperationError(Exception):
    pass
