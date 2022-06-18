print("Build parser")

import ply.yacc as yacc

from lexical_analyser import CC20221Lexer

# Necessário para criar o parser com yacc
lexer = CC20221Lexer()
tokens = lexer.tokens


class CC20221SyntaxError(Exception):
    pass


# TODO: uma mensagem de insucesso indicando qual é a entrada
#  na tabela de reconhecimento sintático que está vazia (qual é a forma sentencial α,
#  qual é o símbolo não-terminal mais à esquerda de α e qual é o token da entrada)
def p_error(p):
    raise CC20221SyntaxError(f"Syntax error in input {str(p)}")


def p_empty(p):
    """empty :"""
    pass


def p_prog_statement(p):
    """PROGRAM  : STATEMENT
    | FUNCLIST
    | empty"""
    # p[0] = p[1]


def p_funclist(p):
    """FUNCLIST : FUNCDEF FUNCLISTAUX"""
    pass


def p_funclistaux(p):
    """FUNCLISTAUX  : FUNCLIST
    | empty"""
    pass


def p_fundef(p):
    """FUNCDEF : DEF IDENT LPARENTHESIS PARAMLIST RPARENTHESIS LCURLYBRACKET STATELIST RCURLYBRACKET"""
    pass


def p_paramlist(p):
    """PARAMLIST    : DATATYPE IDENT PARAMLISTAUX
    | empty"""
    pass


def p_paramlist_aux(p):
    """PARAMLISTAUX : COMMA PARAMLIST
    | empty"""
    pass


def p_datatype(p):
    """DATATYPE : INT
    | FLOAT
    | STRING"""
    pass


def p_statement_vardecl(p):
    """STATEMENT : VARDECL SEMICOLON"""
    pass


def p_statement_atrib(p):
    """STATEMENT : ATRIBSTAT SEMICOLON"""
    pass


def p_statement_print(p):
    """STATEMENT : PRINTSTAT SEMICOLON"""
    pass


def p_statement_read(p):
    """STATEMENT : READSTAT SEMICOLON"""
    pass


def p_statement_return(p):
    """STATEMENT : RETURNSTAT SEMICOLON"""
    pass


def p_statement_if(p):
    """STATEMENT : IFSTAT SEMICOLON"""
    pass


def p_statement_for(p):
    """STATEMENT : FORSTAT SEMICOLON"""
    pass


def p_statement_state(p):
    """STATEMENT : LCURLYBRACKET STATELIST RCURLYBRACKET"""
    pass


def p_statement_term(p):
    """STATEMENT    : BREAK SEMICOLON
    | SEMICOLON"""
    pass


def p_vardecl(p):
    """VARDECL : DATATYPE IDENT OPTIONAL_VEC"""
    pass


def p_optional_vec(p):
    """OPTIONAL_VEC : LBRACKET INT_CONSTANT RBRACKET OPTIONAL_VEC
    | empty"""
    pass


def p_atribstat(p):
    """ATRIBSTAT : LVALUE ASSIGNMENT R_ATRIB"""
    pass


def p_r_atrib(p):
    """R_ATRIB   : EXPRESSION
    | ALLOCEXPRESSION
    | FUNCCALL"""
    pass


def p_funccall(p):
    """FUNCCALL : IDENT LPARENTHESIS PARAMLISTCALL RPARENTHESIS"""
    pass


def p_paramlistcall(p):
    """PARAMLISTCALL : IDENT PARAMLISTCALLAUX"""
    pass


def p_paramlistcall_aux(p):
    """PARAMLISTCALLAUX : COMMA PARAMLISTCALL
    | empty"""
    pass


def p_printstat(p):
    """PRINTSTAT : PRINT EXPRESSION"""
    pass


def p_readstat(p):
    """READSTAT : READ LVALUE"""
    pass


def p_returnstat(p):
    """RETURNSTAT : RETURN"""
    pass


def p_ifstat(p):
    """IFSTAT : IF LPARENTHESIS EXPRESSION RPARENTHESIS STATEMENT IFAUX"""
    pass


def p_ifaux(p):
    """IFAUX    : ELSE STATEMENT
    | empty"""
    pass


def p_forstat(p):
    """FORSTAT : FOR LPARENTHESIS ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPARENTHESIS STATEMENT"""
    pass


def p_statelist(p):
    """STATELIST : STATEMENT OPT_STATELIST"""
    pass


def p_opt_statelist(p):
    """OPT_STATELIST    : STATELIST
    | empty"""
    pass


def p_allocexp(p):
    """ALLOCEXPRESSION : NEW DATATYPE LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION"""
    pass


def p_opt_numexpression(p):
    """OPT_NUMEXPRESSION    : LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION
    | empty"""
    pass


def p_expression(p):
    """EXPRESSION : NUMEXPRESSION OPT_REL_OP_NUM_EXPRESSION"""
    pass


def p_opt_rel_op_num_expression(p):
    """OPT_REL_OP_NUM_EXPRESSION    : REL_OP NUMEXPRESSION
    | empty"""
    pass


def p_relop_lt(p):
    """REL_OP : LESSTHAN"""
    pass


def p_relop_gt(p):
    """REL_OP : GREATERTHAN"""
    pass


def p_relop_lte(p):
    """REL_OP : LESSEQUAL"""
    pass


def p_relop_gte(p):
    """REL_OP : GREATEREQUAL"""
    pass


def p_relop_eq(p):
    """REL_OP : EQUAL"""
    pass


def p_relop_neq(p):
    """REL_OP : DIFFERENT"""
    pass


def p_numexpression(p):
    """NUMEXPRESSION : TERM REC_PLUS_MINUS_TERM"""
    pass


def p_rec_plus_minus_term(p):
    """REC_PLUS_MINUS_TERM : PLUS_OR_MINUS TERM REC_PLUS_MINUS_TERM
    | empty"""
    pass


def p_plus_or_minus(p):
    """PLUS_OR_MINUS    : PLUS
    | MINUS"""
    pass


def p_term(p):
    """TERM : UNARYEXPR OPT_UNARYEXPR"""
    pass


def p_opt_unary_expr(p):
    """OPT_UNARYEXPR    : OPERATOR UNARYEXPR OPT_UNARYEXPR
    | empty"""
    pass


def p_operator(p):
    """OPERATOR : MULT
    | MOD
    | DIV"""
    pass


def p_opt_plus_or_minus(p):
    """OPT_PLUS_MINUS   : PLUS_OR_MINUS
    | empty"""
    pass


def p_unary_exp(p):
    """UNARYEXPR : OPT_PLUS_MINUS FACTOR"""
    pass


def p_factor_const(p):
    """FACTOR : INT_CONSTANT
    | FLOAT_CONSTANT
    | STRING_CONSTANT
    | NULL
    | LVALUE"""
    pass


def p_factor_numexpression(p):
    """FACTOR : LPARENTHESIS NUMEXPRESSION RPARENTHESIS"""
    pass


def p_lvalue(p):
    """LVALUE : IDENT OPT_NUMEXPRESSION"""
    pass


# Constrói parser
parser = yacc.yacc(start="PROGRAM")

from pathlib import Path

EXAMPLES_PATH = Path(__file__).parents[1]

with (EXAMPLES_PATH / "examples/tests/exemplo2.lcc").open("r") as f:
    s = f.read()

result = parser.parse(s, debug=True, lexer=lexer)
print(result)
