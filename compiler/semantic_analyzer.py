import compiler.ply.yacc as yacc
from compiler.lexical_analyzer import CC20221Lexer
from compiler.syntactic_analyzer import CC20221SyntaxError
from compiler.ply.lex import LexToken
from compiler.utils import (BreakOutsideLoopError, Scope, ScopeStack,
                            TableEntry, VariableNotDeclaredError, Node, InvalidTypeOperationError)

from typing import List

class CC20221SemanticAnalyzer:
    '''Semantic Analyser for CC20221 grammar'''

    def __init__(self, **kwargs):
        self.scope_stack = ScopeStack()
        self.tables_list: List[List[TableEntry]] = list()
        self.num_exprs: List[Tuple[Node, int]] = []
        self.lexer = CC20221Lexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(start="PROGRAM", module=self, **kwargs)
        self.global_scope: Optional[Scope] = None

    def p_error(self, p):
        sentence = [
            i.type if isinstance(i, LexToken) else str(i) for i in self.parser.symstack
        ]
        raise CC20221SyntaxError(
            f"Syntax error in symbol {self.parser.symstack[-1]} on token {p} in stack: {' '.join(sentence[1:])}"
        )

    def p_empty(self, p):
        "empty :"
        pass

    def p_new_scope(self, p):
        '''new_scope :'''
        self.create_new_scope(is_loop=False)

    def p_new_scope_loop(self, p):
        '''new_scope_loop :'''
        self.create_new_scope(is_loop=True)

    def p_prog_statement(self, p):
        '''PROGRAM  : new_scope STATEMENT
                    | new_scope FUNCLIST
                    | empty'''
        self.global_scope = self.scope_stack.pop()
        self.tables_list.append(self.global_scope.table)
        assert len(self.scope_stack.stack) == 0, "Could not validating scope completeness"

    def p_funclist(self, p):
        "FUNCLIST : FUNCDEF FUNCLISTAUX"
        pass

    def p_funclistaux(self, p):
        '''FUNCLISTAUX  : FUNCLIST
                        | empty'''
        pass

    def p_funcdef(self, p):
        "FUNCDEF : DEF IDENT new_scope LPARENTHESIS PARAMLIST RPARENTHESIS LCURLYBRACKET STATELIST RCURLYBRACKET"
        # go back to previous scope
        self.tables_list.append(self.scope_stack.pop().table)
        # add function decl
        scope = self.scope_stack.peek()
        entry = TableEntry(p[2], "function", [], p.lineno(2))
        scope.add_table_entry(entry)

    def p_paramlist(self, p):
        '''PARAMLIST    : DATATYPE IDENT PARAMLISTAUX
                        | empty'''
        if len(p) > 2:
            scope = self.scope_stack.peek()
            entry = TableEntry(p[2], p[1], [], p.lineno(2))
            scope.add_table_entry(entry)

    def p_paramlist_aux(self, p):
        '''PARAMLISTAUX : COMMA PARAMLIST
                        | empty'''
        pass

    def p_datatype(self, p):
        '''DATATYPE : INT
                    | FLOAT
                    | STRING'''
        p[0] = p[1].lower()

    def p_statement_vardecl(self, p):
        "STATEMENT : VARDECL SEMICOLON"
        pass

    def p_statement_atrib(self, p):
        "STATEMENT : ATRIBSTAT SEMICOLON"
        pass

    def p_statement_print(self, p):
        "STATEMENT : PRINTSTAT SEMICOLON"
        pass

    def p_statement_read(self, p):
        "STATEMENT : READSTAT SEMICOLON"
        pass

    def p_statement_return(self, p):
        "STATEMENT : RETURNSTAT SEMICOLON"
        pass

    def p_statement_if(self, p):
        "STATEMENT : IFSTAT"
        pass

    def p_statement_for(self, p):
        "STATEMENT : FORSTAT"
        pass

    def p_statement_statelist(self, p):
        "STATEMENT : new_scope LCURLYBRACKET STATELIST RCURLYBRACKET"
        self.tables_list.append(self.scope_stack.pop().table)
        

    def p_statement_term(self, p):
        '''STATEMENT    : BREAK SEMICOLON
                        | SEMICOLON'''
        if len(p) > 1:
            current_scope = self.scope_stack.peek()
            while True:
                if current_scope.is_loop:
                    break
                current_scope = current_scope.parent_scope
                if current_scope is None:
                    raise BreakOutsideLoopError(p.lineno(2))

    def p_vardecl(self, p):
        "VARDECL : DATATYPE IDENT OPTIONAL_VEC"
        entry = TableEntry(p[2], p[1], p[3], p.lineno(2))
        scope = self.scope_stack.peek()
        scope.add_table_entry(entry)

    def p_optional_vec(self, p):
        '''OPTIONAL_VEC : LBRACKET INT_CONSTANT RBRACKET OPTIONAL_VEC
                        | empty'''
        pass

    def p_atribstat(self, p):
        "ATRIBSTAT : LVALUE ASSIGNMENT R_ATRIB"
        pass

    def p_r_atrib(self, p):
        '''R_ATRIB  : EXPRESSION
                    | ALLOCEXPRESSION
                    | FUNCCALL'''
        pass

    def p_funccall(self, p):
        "FUNCCALL : IDENT LPARENTHESIS PARAMLISTCALL RPARENTHESIS"
        pass

    def p_paramlistcall(self, p):
        "PARAMLISTCALL : IDENT PARAMLISTCALLAUX"
        pass

    def p_paramlistcall_aux(self, p):
        '''PARAMLISTCALLAUX : COMMA PARAMLISTCALL
                            | empty'''
        pass

    def p_printstat(self, p):
        "PRINTSTAT : PRINT EXPRESSION"
        pass

    def p_readstat(self, p):
        "READSTAT : READ LVALUE"
        pass

    def p_returnstat(self, p):
        "RETURNSTAT : RETURN"
        pass

    def p_ifstat(self, p):
        "IFSTAT : IF LPARENTHESIS EXPRESSION RPARENTHESIS new_scope STATEMENT IFAUX"
        self.tables_list.append(self.scope_stack.pop().table)

    def p_ifaux(self, p):
        '''IFAUX    : ELSE new_scope STATEMENT
                    | empty'''
        if len(p) > 2:
            self.tables_list.append(self.scope_stack.pop().table)

    def p_forstat(self, p):
        "FORSTAT : FOR LPARENTHESIS ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPARENTHESIS new_scope_loop STATEMENT"
        self.tables_list.append(self.scope_stack.pop().table)

    def p_statelist(self, p):
        "STATELIST : STATEMENT OPT_STATELIST"
        pass

    def p_opt_statelist(self, p):
        '''OPT_STATELIST    : STATELIST
                            | empty'''
        pass

    def p_allocexp(self, p):
        "ALLOCEXPRESSION : NEW DATATYPE LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION"
        # num_expressions.append((p[4]['node'], p.lineno(1)))

    def p_opt_numexpression(self, p):
        '''OPT_NUMEXPRESSION    : LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION
                                | empty'''
        if len(p) < 3:
            p[0] = ''
        else:
            p[0] = '[' + str(p[2]) + ']' + p[4]

            # num_expressions.append((p[2]['node'], p.lineno(1)))

    def p_expression(self, p):
        "EXPRESSION : NUMEXPRESSION OPT_EXPRESSION"
        # self.num_exprs.append((p[1]['node'], p.lineno(1)))

    def p_opt_expression(self, p):
        '''OPT_EXPRESSION    : REL_OP NUMEXPRESSION
                                        | empty'''
        pass

    def p_relop_lt(self, p):
        '''REL_OP   : LESSTHAN
                    | GREATERTHAN
                    | LESSEQUAL
                    | GREATEREQUAL
                    | EQUAL
                    | DIFFERENT'''
        pass

    def p_numexpression(self, p):
        "NUMEXPRESSION : TERM OTHERTERM"
        # if p[2] is None:
        #     p[0] = p[1]
        # else:
        #     result_type = self.check_type(
        #         p[1]['node'],
        #         p[2]['node'],
        #         p[2]['operation'],
        #         p.lineno(1),
        #     )
        #     p[0] = {
        #         'node': Node(
        #             p[1]['node'],
        #             p[2]['node'],
        #             p[2]['operation'],
        #             result_type,
        #         )
        #     }

    def p_otherterm_empty(self, p):
        '''OTHERTERM    : empty'''
        p[0] = None

    def p_otherterm(self, p):
        '''OTHERTERM    : PLUS_OR_MINUS TERM OTHERTERM'''
        # if p[3]:
        #     result_type = self.check_type(
        #         p[2]['node'],
        #         p[3]['node'],
        #         p[1]['operation'],
        #         p.lineno(1),
        #     )
        #     p[0] = {
        #         'node': Node(
        #             p[2]['node'],
        #             p[3]['node'],
        #             p[1]['operation'],
        #             result_type,
        #         )
        #     }
        # else:
        #     p[0] = {
        #         'node': p[2]['node'],
        #         'operation': p[1]['operation']
        #     }

    def p_plus_or_minus(self, p):
        '''PLUS_OR_MINUS    : PLUS
                            | MINUS'''
        p[0] = {'operation': p[1]}

    def p_term(self, p):
        "TERM : UNARYEXPR OPT_UNARYEXPR"
        # if p[2]: # has another operation
        #     op1 = p[1]['node'],
        #     op2 = p[2]['node'],
        #     op = p[2]['operation'],
        #     result_type = self.check_type(
        #         op1, op2, op,
        #         p.lineno(1),
        #     )
        #     p[0] = {
        #         'node': Node(op1, op2, op, result_type),
        #         'operation': op,
        #     }
        # else: # send node upwards
        #     p[0] = {
        #         'node': p[1]['node']
        #     }
            

    def p_opt_unary_expr_mult(self, p):
        '''OPT_UNARYEXPR    : MULT UNARYEXPR OPT_UNARYEXPR'''
        p[0] = {
            'node': p[2]['node'],
            'operation': '*',
        }

    def p_opt_unary_expr_mod(self, p):
        '''OPT_UNARYEXPR    : MOD UNARYEXPR OPT_UNARYEXPR'''
        p[0] = {
            'node': p[2]['node'],
            'operation': '%',
        }

    def p_opt_unary_expr_div(self, p):
        '''OPT_UNARYEXPR    : DIV UNARYEXPR OPT_UNARYEXPR'''
        p[0] = {
            'node': p[2]['node'],
            'operation': '%',
        }

    def p_opt_unary_expr(self, p):
        '''OPT_UNARYEXPR    : empty'''
        p[0] = None

    def p_unary_exp(self, p):
        '''UNARYEXPR    : MINUS FACTOR
                        | FACTOR'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[2]['node'].value *= -1
            p[0] = p[2]

    def p_factor_lvalue_const(self, p):
        '''FACTOR : LVALUE'''
        p[0] = p[1]

    def p_factor_null_const(self, p):
        '''FACTOR : NULL'''
        p[0] = {'node': Node(None, None, None, 'null')}

    def p_factor_string_const(self, p):
        '''FACTOR : STRING_CONSTANT'''
        p[0] = {'node': Node(None, None, p[1], 'string')}

    def p_factor_float_const(self, p):
        '''FACTOR : FLOAT_CONSTANT'''
        p[0] = {'node': Node(None, None, p[1], 'float')}
        
    def p_factor_int_const(self, p):
        '''FACTOR : INT_CONSTANT'''
        p[0] = {'node': Node(None, None, p[1], 'int')}
        
    def p_factor_numexpression(self, p):
        "FACTOR : LPARENTHESIS NUMEXPRESSION RPARENTHESIS"
        p[0] = p[2]
        # self.num_exprs.append(p[2]['node'], p.lineno(1))

    def p_lvalue(self, p):
        "LVALUE : IDENT OPT_NUMEXPRESSION"
        self.get_variable_type(p[1], p.lineno(1))
        p[0] = {
            'node' : Node(None, None, p[1] + p[2], result_type=self.get_variable_type(p[1], p.lineno(1)))
        }

    def parse(self, source_code: str, **kwargs):
        try:
            self.parser.parse(source_code, lexer=self.lexer, **kwargs)
            self.print_symbol_table()
        except CC20221SyntaxError as e:
            return "failed with syntax errors"
        return "success"

    def print_symbol_table(self) -> None:
        for i, table_entry_list in enumerate(self.tables_list):
            print("table", i)
            for table_entry in table_entry_list:
                print(table_entry.identifier, 'type:', table_entry.datatype)
            print()

    def create_new_scope(self, is_loop: bool) -> None:
        '''Creates new scope on top of the current scope'''
        top_scope = self.scope_stack.peek()
        new_scope = Scope(parent_scope=top_scope, is_loop=is_loop)
        if top_scope:
            top_scope.add_to_inner(new_scope)
        self.scope_stack.push(new_scope)

    def get_variable_type(self, identifier: str, lineno: int) -> None:
        '''Find variable type in symbol table'''
        scope = self.scope_stack.peek()
        while True:
            for entry in scope.table:
                if entry.identifier == identifier:
                    return entry.datatype
            scope = scope.parent_scope
            if scope is None:
                raise VariableNotDeclaredError(f"{identifier} in line {lineno} is not in scope.")

    def check_type(self, left, right, op, lineno):
        valids = {
            ('string', '+', 'string'): 'string',
            ('string', '*', 'string'): 'string',
            ('int', '+', 'int'): 'int',
            ('int', '-', 'int'): 'int',
            ('int', '*', 'int'): 'int',
            ('int', '%', 'int'): 'int',
            ('int', '/', 'int'): 'float',
            ('float', '+', 'float'): 'float',
            ('float', '-', 'float'): 'float',
            ('float', '*', 'float'): 'float',
            ('float', '/', 'float'): 'float',
            ('float', '+', 'int'): 'float',
            ('float', '-', 'int'): 'float',
            ('float', '*', 'int'): 'float',
            ('float', '/', 'int'): 'float',
            ('int', '+', 'float'): 'float',
            ('int', '-', 'float'): 'float',
            ('int', '*', 'float'): 'float',
            ('int', '/', 'float'): 'float',
        }
        result = valids.get(
            (left.result_type, op, right.result_type), None)

        # if result is None:
            # raise InvalidTypeOperationError(
                # f'{left.result_type},{right.result_type},{lineno}')

        return result